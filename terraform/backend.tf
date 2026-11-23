
terraform {
  backend "s3" {
    bucket       = "cloudops-tfstate-176550299744-eu-west-1-an"
    key          = "cloudops/terraform.tfstate"
    region       = "eu-west-1"
    encrypt      = true
    use_lockfile = true
  }
}
