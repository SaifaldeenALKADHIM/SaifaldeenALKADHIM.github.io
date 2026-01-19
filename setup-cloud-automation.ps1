#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Automated GitHub Token Setup for Cloud Auto-Posting
    
.DESCRIPTION
    This script automates the token update process for GitHub Actions
    twice-daily automation without needing your laptop to be on.
    
.EXAMPLE
    .\setup-cloud-automation.ps1
#>

Write-Host "================================" -ForegroundColor Cyan
Write-Host "☁️  GitHub Actions Cloud Setup" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "📌 IMPORTANT:" -ForegroundColor Yellow
Write-Host "1. Go to: https://github.com/settings/tokens" -ForegroundColor White
Write-Host "2. Click 'Generate new token' → 'Tokens (classic)'" -ForegroundColor White
Write-Host "3. Select scopes: repo, workflow, read:user, public_repo" -ForegroundColor White
Write-Host "4. Click 'Generate token'" -ForegroundColor White
Write-Host ""

$token = Read-Host "Paste your new GitHub token"

if ($token -notmatch '^ghp_') {
    Write-Host "Invalid token! Must start with ghp_" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "🔄 Updating git remote..." -ForegroundColor Cyan

try {
    $remote = "https://$($token)@github.com/SaifaldeenALKADHIM/SaifaldeenALKADHIM.github.io.git"
    git remote set-url origin $remote
    Write-Host "✅ Git remote updated successfully" -ForegroundColor Green
}
catch {
    Write-Host "❌ Failed to update git remote" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "🚀 Pushing workflow automation to GitHub..." -ForegroundColor Cyan

try {
    git push
    Write-Host "✅ Push successful!" -ForegroundColor Green
}
catch {
    Write-Host "❌ Push failed" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "================================" -ForegroundColor Green
Write-Host "✅ Setup Complete!" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Green
Write-Host ""
Write-Host "🎉 Your cloud automation is now active!" -ForegroundColor Cyan
Write-Host ""
Write-Host "📅 Schedule:" -ForegroundColor White
Write-Host "   • 9 AM UTC (10 AM Budapest) - Morning posts" -ForegroundColor Gray
Write-Host "   • 9 PM UTC (10 PM Budapest) - Evening posts" -ForegroundColor Gray
Write-Host ""
Write-Host "📊 Expected daily output: 14+ new research posts" -ForegroundColor White
Write-Host ""
Write-Host "✨ Your blog will update automatically even with laptop OFF!" -ForegroundColor Cyan
Write-Host ""
Write-Host "📍 Monitor your workflow:" -ForegroundColor White
Write-Host "   https://github.com/SaifaldeenALKADHIM/SaifaldeenALKADHIM.github.io/actions" -ForegroundColor Blue
