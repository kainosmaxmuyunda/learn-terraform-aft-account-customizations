variable "name" {
  default     = "Default"
  type        = string
  description = "Name of the VPC"
}

variable "project" {
    default   = "Dev"
  type        = string
  description = "Name of project this VPC is meant to house"
}

variable "environment" {
    default   = "Landing zone"
  type        = string
  description = "Name of environment this VPC is targeting"
}

variable "region" {
  default     = "eu-west-2"
  type        = string
  description = "Region of the VPC"
}

variable "cidr_block" {
  default     = "10.0.0.0/16"
  type        = string
  description = "CIDR block for the VPC"
}

variable "public_subnet_cidr_blocks" {
  default     = ["10.0.0.0/24", "10.0.2.0/24"]
  type        = list(any)
  description = "List of public subnet CIDR blocks"
}

variable "private_subnet_cidr_blocks" {
  default     = ["10.0.1.0/24", "10.0.3.0/24"]
  type        = list(any)
  description = "List of private subnet CIDR blocks"
}

variable "availability_zones" {
  default     = ["eu-west-2a", "eu-west-2b"]
  type        = list(any)
  description = "List of availability zones"
}

variable "tags" {
  default     = {}
  type        = map(string)
  description = "Extra tags to attach to the VPC resources"
}