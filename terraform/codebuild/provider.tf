terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
  required_version = ">=1.4.4"
}

# Configure the AWS Provider
provider "aws" {
  region              = "eu-west-2"
  allowed_account_ids = local.variables.allowed_account_ids

  default_tags {
    tags = local.tags
  }
}

terraform {
  backend "s3" {
  }
}