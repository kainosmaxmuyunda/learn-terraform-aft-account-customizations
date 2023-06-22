resource "aws_ssm_parameter" "foo" {
  name = "/accID"
  type = "string"
  value = "${data.aws_caller_identity.current.account_id}"
}