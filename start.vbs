
Dim oShell

Set oShell = WScript.CreateObject ("WSCript.shell")

oShell.run "start.bat",0

Set oShell = Nothing