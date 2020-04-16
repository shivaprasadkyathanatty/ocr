import paramiko
#connecting to aws
key = paramiko.RSAKey.from_private_key_file("/home/shivaprasad/ace-aws1.pem")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
stdin, stdout, stderr = client.exec_command("aws s3 cp s3://iclicker-ocr/raw_image/ /mnt/iclicker_ocr/raw_images/ --recursive")

 