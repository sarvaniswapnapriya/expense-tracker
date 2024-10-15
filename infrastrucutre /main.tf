# infrastructure/main.tf

provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  # Missing required attribute "count"
}

resource "aws_s3_bucket" "bucket" {
  bucket = "my-bucket"
  acl    = "invalid_acl"  # This should be a valid ACL
}
