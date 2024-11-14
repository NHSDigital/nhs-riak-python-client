# CodeBuild Terraform

## Description
The Terraform in this folder configures the CodeBuild instance in AWS and sets up the necessary
permissions for builds to be created from GitHub actions.

The Terraform is not automatically deployed and any changes must be manually applied from the
developer's machine. Instructions for doing this are in the section below

## Changing the Terraform

After making the necessary changes to the Terraform config, the changes will need to be manually
applied so that the resources in AWS are updated.

The first step is to assume an AWS role so that you have the correct credentials to run the
terraform commands. Assuming that you have set up Granted as suggested [on this
page](https://nhsd-confluence.digital.nhs.uk/display/SPINE/Spine+in+the+Cloud+-+Terraform+developer+setup),
then you should be able to assume a `NHS-Digital-DDC-Spine-Core-Dev/*` role by running:
```bash
assume -x
```

After that, you need to change into the `terraform/codebuild/` directory in this repo:
```bash
cd terraform/codebuild/
```

And you can now run the following commands to apply your changes to AWS:
```bash
terraform init --backend-config=env/dev.conf
terraform workspace select dev
terraform plan
# Assure that you are happy with the results of the plan before you proceed to apply the changes
terraform apply
```
