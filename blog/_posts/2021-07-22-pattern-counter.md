---
layout: long-post
tag: tool
featured-image: /assets/2021-07-22/pattern-counter.jpg
---
A stitch counting/pattern tracking app<!--more-->.

My favorite thing about knitting and crochet is that they are some of the most simple, relaxing, and meditative hobbies--so much so that the biggest challenge is simply counting stitches and keeping track of your pattern! And while complaining about counting may seem silly, I think most stitchers would agree that having to keep track of stitches (and loosing count of them) can quickly become an incredibly frustrating part of an otherwise idyllic experience. *Pattern Counter* is a tool I made to help allieviate this problem.

[Pattern Counter](https://goldinvo.com/pattern-counter) as a reference is a flexible and interactive web application that can interpret your patterns, so that it can hold your place and keep track of stitch/repeat counts as you use it. It's great for those (like me) who like to stitch in short bursts who lose their in between sessions. It is ideal for managing complex patterns, but I find its also nice to use for simple patterns to mark which row/direction I am on.

## Using the Pattern Counter

When you first open the page (assuming its the first time opening the app on your computer), the pattern form should by default filled with the following pattern: 

```text
Press the 'Next' button or spacebar to advance!

4. sc 3, hdc, dc 3, hdc, sc 3
5. (sc 3, dc 5) * 3 (24 sts) (parenthesis without commas or periods are ignored)

On the next instruction try using the 'Complete Repeat' button! 

6. ((sc 2, dec, sc 2, dec) * 5, sc) * 3

You can also type into the counter display to edit counts directly!

7. ((sc, dc, sc) * 594, sc 3, dc 2) * 2 (Click on the orange counter number and type in something else)

Switch to a G hook (Instructions don't have to start with a number)

You will need to use the 'Exit repeat' button in the next instruction

8. (sc 3, picot) until end of row, sc, hdc, dc

Cut and weave in ends (Now try your own pattern!)
```

Stepping through this example should give you enough intuition about the tool to start using other patterns. When using the different buttons, keep note of how they change the different repeat counts, and how it changes your position relative to where you currently are. Also, see how the tool acts as expected when you type in different numbers into the counters. Also note the format of the input pattern itself, such as how instruction numbers are written, how comments are written (without separators!), and how newline characters are significant.

For more specific details, see the following section.

## Pattern Counter Details

### Symbols

- Instruction Number: `5)`,  `6.`
- Information/Comments: `(30)`, `(You should have 3 stitches on the needle)`, `()`
- Number: `1`, `2`
- String: `sc 3`, `m1r`, `make a magic loop`
- Open Parenthesis: `(`, `{`, `[`
- Closed Parenthesis: `)` `}`, `]`
- Multipliers: `*`
- Seperators: `.`, `,`
- Line Breaks: `↵`

### Symbol Usage

The pattern input by the user should be a sequence of instructions separated by one or more line breaks. Instructions are displayed one at a time, and are composed of the instruction number, comments, sequences of strings, and parenthesis/numbers/multipliers used to denote repeats. 

For example:    

    26. CTC, INC 10, CTB, INC * 20 (60)↵    
    27. CTC, (SC 9, INC) * 2, CTB, (SC 9, INC) * 4  (66)↵    
    ↵    
    28. (CTC, SC 23, CTB, SC 43) * 2 (66)↵    
    39. (CTC, SC 24, CTB, SC 42) * 2 (66)    

Instruction Numbers and Information/Comments are ignored by the application, but are kept in to be displayed as useful information for the user.    
Instruction numbers are optional, and may appear only at the beginning of an instruction if used. 

Strings (which act as a single step when working in a pattern are separated by separators, typically commas, or other symbols. They may consist of numbers but they cannot be only a number.    
- A single string is not wrapped in parenthesis. `(things like this)` are interpreted as a comment.
- A sequence of strings wrapped in parenthesis `(like, this, one)` are interpreted as a repeat sequence.
  - if followed by a multiplier and then by a number `(like, this) * 3`, the sequence will be repeated 3 times as the user steps through them
  - if not followed by both a multiplier and a number, the sequence will repeat indefinitely until the user clicks the "exit repeat" button. This is to account for conditional repeats, such as "until you reach the end of the row" while still being able to keep track of the number of repeats you have made.

### Functions

A few different buttons to traverse the pattern are available, since often we do not need to look at the pattern constantly in order to follow it (having to press the 'next' button after every single step would be tedious). The following buttons are available to step through the pattern in a flexible way:
- `Next (Space)`: go to the next string in accordance to repeat logic (add repeats/go to beginning of repeats/exit repeats as appropriate).
- `Complete Repeat (c)`: acts the same as pressing 'Next' until you either go to the beginning of a repeat sequence, or exit a repeat sequence.
- `Exit Repeat (v)`: finishes the current repeat sequence and drops the repeat's corresponding counter.
- `Undo (ctrl-z)`: goes to the state previous to the last user action (also works on manual counter changes).
- `Next Instruction`: goes to the next instruction in the pattern (as delimited by line breaks).




