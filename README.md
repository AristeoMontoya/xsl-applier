# xsl-applier
Quick python program to apply an XSL to a HTML

Zero validations since it is a quick and dirty CLI tool.

# Setup
` pip install -r requirements.txt`

# Usage
```
positional arguments:
  target                Source file
  xsl                   XSL file

options:
  -o OUTPUT, --output OUTPUT
                        Output file


CLI Command Example:

python app.py <filename_with_extension> <xsl_filename_with_extension>

filename_with_extension = en-US-V-K0059110421_america-34.html
xsl_filename_with_extension = genpage_51.xsl

Result:
python app.py en-US-V-K0059110421_america-34.html genpage_51.xsl


How to use:
1 - Put target and xls file in the same location where the app.py script is. 
2 - Open powershell/gitbash in the same location where the files are.
3 - Type the complete command and execute it.

```