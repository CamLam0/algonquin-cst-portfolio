# Program name: ManyUsers.ps1
# Description: PowerShell script to create 100 users on Active Directory controlled host.
# Author: Cameron Lamoureux
# version 1.0

# Import the Active Directory module
Import-Module ActiveDirectory

# Set the common password for all users
$Password = ConvertTo-SecureString "P@ssWord" -AsPlainText -Force

# Loop to create 100 users
for ($i = 1; $i -le 100; $i++) {
    $Username = "Win11-$i"
    
    New-ADUser -Name $Username `
               -SamAccountName $Username `
               -UserPrincipalName "$Username@lamo0318.lab" `
               -AccountPassword $Password `
               -Enabled $true
    
    Write-Host "Created user: $Username"
}
