# PowerShell script to create a distribution package
$releaseDir = "release"
$zipName = "2048_Game_Windows.zip"

Write-Host "Creating distribution package..." -ForegroundColor Green

# Remove existing zip if it exists
if (Test-Path $zipName) {
    Remove-Item $zipName
    Write-Host "Removed existing zip file" -ForegroundColor Yellow
}

# Create zip file
try {
    Compress-Archive -Path "$releaseDir\*" -DestinationPath $zipName -CompressionLevel Optimal
    Write-Host "✓ Created $zipName successfully!" -ForegroundColor Green
    
    # Get file size
    $size = (Get-Item $zipName).Length / 1MB
    Write-Host "✓ Package size: $([math]::Round($size, 1)) MB" -ForegroundColor Cyan
    
    Write-Host "`nDistribution package ready!" -ForegroundColor Green
    Write-Host "You can now share the $zipName file with others." -ForegroundColor White
    
    # Show contents
    Write-Host "`nPackage contents:" -ForegroundColor Yellow
    Get-ChildItem $releaseDir | ForEach-Object { Write-Host "  - $($_.Name)" -ForegroundColor White }
    
} catch {
    Write-Host "❌ Error creating zip file: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host "`nPress any key to continue..."
$host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
