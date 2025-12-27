# Note: Script derived from Microsoft Learn platform while learning about user creation in PowerShell.
# Description: Create a user from user-provided credentials. Run with elevated permissions.
$Password = Read-Host "Enter password: " -AsSecureString

$params = @{
  Name = Read-Host "Enter username:"
  FullName = "Test User"
  Password = $Password
  Description = "Created via script NewUser.ps1"
}

New-LocalUser @params
Add-LocalGroupMember -Name Users -Member $params[0]
