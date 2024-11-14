locals {
  name        = "riak-python-client"
  environment = terraform.workspace
  variables   = jsondecode(file("${path.module}/env/${local.environment}.json"))

  git_url    = "https://github.com/NHSDigital/spine-riak-python-client"
  git_branch = "master"

  tags = {
    TagVersion         = "1"
    Programme          = "SpineCore"
    Project            = "RIAKPYTHONCLIENT"
    DataClassification = local.environment == "prod" ? "5" : "1"
    Environment        = local.environment
    ServiceCategory    = local.environment == "prod" ? "Bronze" : "N/A"
    Tool               = "terraform"
  }
}


data "aws_caller_identity" "current" {}
data "aws_region" "current" {}
