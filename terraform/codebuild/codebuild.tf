data "aws_iam_policy_document" "instance_assume_role_policy" {
  statement {
    effect  = "Allow"
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["codebuild.amazonaws.com"]
    }
  }
}
resource "aws_iam_role" "spine_riak_python_client_iam_role" {
  name               = "${local.environment}-${local.name}-codebuild-role"
  path               = "/service-role/"
  assume_role_policy = data.aws_iam_policy_document.instance_assume_role_policy.json
}

data "aws_iam_policy_document" "codebuild" {
  statement {
    effect = "Allow"

    actions = [
      "logs:CreateLogGroup",
      "logs:CreateLogStream",
      "logs:PutLogEvents",
    ]

    resources = [
      "arn:aws:logs:${data.aws_region.current.id}:${data.aws_caller_identity.current.account_id}:log-group:/aws/codebuild/${local.name}*:*"
    ]
  }

  # tfsec:ignore:aws-iam-no-policy-wildcards
  statement {
    effect = "Allow"

    actions = [
      "ec2:CreateNetworkInterface",
      "ec2:DescribeDhcpOptions",
      "ec2:DescribeNetworkInterfaces",
      "ec2:DeleteNetworkInterface",
      "ec2:DescribeSubnets",
      "ec2:DescribeSecurityGroups",
      "ec2:DescribeVpcs"
    ]

    resources = [
      "*"
    ]

    condition {
      test     = "ArnLikeIfExists"
      variable = "ec2:Vpc"
      values   = ["arn:aws:ec2:${data.aws_region.current.id}:${data.aws_caller_identity.current.account_id}:vpc/${local.variables.build_vpc}"]
    }

  }

  statement {
    effect = "Allow"

    actions = [
      "ec2:CreateNetworkInterfacePermission"
    ]

    resources = [
      "arn:aws:ec2:${data.aws_region.current.id}:${data.aws_caller_identity.current.account_id}:network-interface/*"
    ]

    condition {
      test     = "StringEquals"
      variable = "ec2:Subnet"
      values = [
        "arn:aws:ec2:${data.aws_region.current.id}:${data.aws_caller_identity.current.account_id}:subnet/${local.variables.build_private_subnets[0]}",
        "arn:aws:ec2:${data.aws_region.current.id}:${data.aws_caller_identity.current.account_id}:subnet/${local.variables.build_private_subnets[1]}",
        "arn:aws:ec2:${data.aws_region.current.id}:${data.aws_caller_identity.current.account_id}:subnet/${local.variables.build_private_subnets[2]}"
      ]
    }

    condition {
      test     = "StringEquals"
      variable = "ec2:AuthorizedService"
      values   = ["codebuild.amazonaws.com"]
    }

  }

  statement {
    actions = [
      "ssm:GetParameters"
    ]
    resources = [
      "arn:aws:ssm:${data.aws_region.current.id}:${data.aws_caller_identity.current.account_id}:parameter${local.variables.nexus_password_path}"
    ]
  }

}

resource "aws_iam_policy" "codebuild" {
  name   = "CodeBuildBasePolicy-${local.environment}-${local.name}-codebuild"
  path   = "/service-role/"
  policy = data.aws_iam_policy_document.codebuild.json
}

resource "aws_iam_role_policy_attachment" "codebuild" {
  role       = aws_iam_role.spine_riak_python_client_iam_role.name
  policy_arn = aws_iam_policy.codebuild.arn
}

resource "aws_codebuild_project" "spine-riak-python-client-codebuild" {
  name          = "${local.environment}-${local.name}-codebuild"
  service_role  = aws_iam_role.spine_riak_python_client_iam_role.arn
  build_timeout = 30

  artifacts {
    type = "NO_ARTIFACTS"
  }

  environment {
    compute_type                = local.variables.compute_type
    image                       = "aws/codebuild/standard:6.0"
    type                        = "LINUX_CONTAINER"
    image_pull_credentials_type = "CODEBUILD"
    privileged_mode             = true

    environment_variable {
      name  = "NEXUS_URL"
      value = "https://nexus.devspineservices.nhs.uk/repository/spine-pypi/"
    }

    environment_variable {
      name  = "NEXUS_USERNAME"
      value = "spineii"
    }

    environment_variable {
      name  = "NEXUS_PASSWORD"
      value = local.variables.nexus_password_path
      type  = "PARAMETER_STORE"
    }

    environment_variable {
      name  = "PIP_INDEX_ARGS"
      value = "--index-url=https://nexus.devspineservices.nhs.uk/repository/pypi-proxy/simple --extra-index-url=https://nexus.devspineservices.nhs.uk/repository/spine-pypi/simple"
    }
  }

  logs_config {
    cloudwatch_logs {
      group_name = "/aws/codebuild/${local.name}"
    }
  }

  source {
    type            = "GITHUB"
    location        = local.git_url
    git_clone_depth = 1
    buildspec       = "deploy/release-buildspec.yaml"

    git_submodules_config {
      fetch_submodules = false
    }
  }

  source_version = local.git_branch

  vpc_config {
    vpc_id             = local.variables.build_vpc
    subnets            = local.variables.build_private_subnets
    security_group_ids = [aws_security_group.codebuild_sg.id]
  }

}

#tfsec:ignore:aws-ec2-no-public-egress-sgr
resource "aws_security_group" "codebuild_sg" {
  name        = "${local.environment}-${local.name}-codebuild-sg"
  vpc_id      = local.variables.build_vpc
  description = "Codebuild Internal Security Group"

  egress {
    description = "Allow all"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
