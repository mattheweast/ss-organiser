-- Read the screenshot count from the temporary file
set tempFile to (POSIX path of (path to home folder)) & "screenshot_count.txt"
set screenshotCount to (do shell script "cat " & quoted form of tempFile)

-- Display the notification
display notification "You have organised and removed " & screenshotCount & " screenshots from your desktop." with title "Screenshot Organiser"

-- Optionally, delete the temporary file
do shell script "rm " & quoted form of tempFile
