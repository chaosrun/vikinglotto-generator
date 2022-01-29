# vikinglotto-generator

This program generates a set of randomly picked 
[Vikinglotto](https://en.wikipedia.org/wiki/Vikinglotto) lottery numbers.

The program's output supports showing the findings using 'cowsay' for added interest.
The generated numbers are stored in a log file and can be reviewed if necessary. 

## Requirements

If you need the program to display the results as `cowsay`, you need to have `cowsay` installed on your system.

Take Debian & Ubuntu as an example:

```bash
sudo apt update
sudo apt install cowsay -y
```

## Usage

Run the program in `cowsay` mode:

```bash
python main.py
```

Without using `cowsay`, print the result directly:

```bash
python main.py --plain
```
