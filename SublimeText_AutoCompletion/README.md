# Overview
This directory has the configuration file needed, to have auto completion inside Sublime Text for Lua script used in [Command: Modern Operations](https://www.matrixgames.com/game/command-modern-operations) (C:MO).

## Completion Status
- Functions (Functional but no documentation)
	- Only set for auto completion
	- No argument place holders
	- No Annotations
	- No Description 
- Types
	- Fully implemented


## Content when finished
The following C:MO specific Lua script components will be inside the auto completion:
- Functions
	- Function name (Triggers completion)
	- Argument placeholder that the cursor jumps to it, for better coding flow
	- Input and Output
	- Short description what the function does
- Types
	- Type name (Triggers completion)
	- Short description of the type


## How to install auto completion for CommandLua in Sublime Text
1. Copy the lua directory into:
	- Linux: `/home/{YOUR_USER}/.config/sublime-text/Packages/User`.
 	- Windows: `%APPDATA%\Sublime Text 3\Packages` 
3. You can also go to this directory via GUI, by clicking `Preferences` and then `Browse Packages...`
4. Check that the `.sublime-completions` file is inside the lua directory (Maybe you need to activte the "Show Hidden Files" option in your file explorer)
5. You should now have the auto completions inside Lua-Files (Ctrl+Shift+P then type `syntax lua` and hit enter, this sets the syntax of your file to Lua)

## Source for auto completion
- [CommandLua Documentation](https://commandlua.github.io/index.html)
- [Sublime Completion Documentation](https://www.sublimetext.com/docs/completions.html)
