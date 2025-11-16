# Overview
This directory has the configuration file needed, to have auto completion inside Sublime Text for Lua script used in [Command: Modern Operations](https://www.matrixgames.com/game/command-modern-operations) (C:MO).

The following C:MO specific Lua script components are inside the auto completion:
- Functions
	- Function name (Triggers completion)
	- Argument placeholder that the cursor jumps to it, for better coding flow
	- Input and Output
	- Short description what the function does
- Types
	- Type name (Triggers completion)
	- Short description of the type


## How to install auto completion for CommandLua in Sublime Text
1. Copy the lua directory into `/home/{YOUR_USER}/.config/sublime-text/Packages/User`.
2. You can also go to this directory via GUI, by clicking `Preferences` and then `Browse Packages...`
3. Check that the `.sublime-completions` file is inside the lua directory (Maybe you need to activte the "Show Hidden Files" option in your file explorer)
4. You should now have the auto completions inside Lua-Files (Ctrl+Shift+P then type `syntax lua` and hit enter, this sets the syntax of your file to Lua)

## Source for auto completion
- [CommandLua Documentation](https://commandlua.github.io/index.html)
- [Sublime Completion Documentation](https://www.sublimetext.com/docs/completions.html)