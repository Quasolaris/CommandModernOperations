# How to install auto completion for CMO Lua in Sublime Text
1. Copy the lua directory into `/home/{YOUR_USER}/.config/sublime-text/Packages/User`.
2. You can also go to this directory via GUI, by clicking `Preferences` and then `Browse Packages...`
3. Check that the `.sublime-completions` file is inside the lua directory (Maybe you need to activte the "Show Hidden Files" option in your file explorer)
4. You should now have the auto completions inside Lua-Files (Ctrl+Shift+P teh type `syntax lua` and hit enter, this sets the syntax of your file to Lua)

## Source for auto completion
- [CommandLua Documentation](https://commandlua.github.io/index.html)
- [Sublime Completion Documentation](https://www.sublimetext.com/docs/completions.html)