#Raspberry Pi SainSmart Relay Module Interface Board

## Overview

This interface board will allow you to connect your Raspberry Pi (rev 2.0, at least) to a [SainSmart 8-Channel 5V Relay Module](http://www.amazon.com/gp/product/B0057OC5WK/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B0057OC5WK&linkCode=as2&tag=fixedd-20).

## Parts List

| Quantity | Part                             | Notes |
| :------: | -------------------------------- | ----- |
| 8        | 12kΩ ¼ Watt Resistors            |       |
| 8        | 10kΩ ¼ Watt Resistors            |       |
| 8        | 2N3904 Transistors               | I used [these](http://www.mouser.com/Search/ProductDetail.aspx?R=2N3904TAvirtualkey51210000virtualkey512-2N3904TA). |
| 1        | 2 inch x 2 inch single-sided PCB | I cut [this](http://www.amazon.com/gp/product/B000P7ALZC/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B000P7ALZC&linkCode=as2&tag=fixedd-20) down. |
| 1        | 3 inch jumper wire               |       |
| 1        | 26 pin header (2x13)             |       |
| 1        | 10 pin header (1x10)             |       |

## Explanation

The SainSmart board is powered by 5v and the relays are triggered by taking the input pin to ground. Since the Raspberry Pi's GPIO pins output 3.3v I used a set of transistors to take the relay pins to ground.

I used 2N3904 transistors simply because they were cheap and readily available. In theory any NPN transistor should work, but the resistors may need to be adjusted.

To make the board I used the toner transfer method. There are [plenty of instructions](http://www.instructables.com/id/Cheap-and-Easy-Toner-Transfer-for-PCB-Making/) on the internet for this, so I won't go into it here.

The Sainsmart Relay Module has opto-isolation on the input pins. To maintain this isolation you would need to use an external 5v power supply.

### Files

* ```eagle_files``` - Provided here are [Eagle PCB](http://www.cadsoftusa.com/eagle-pcb-design-software/) schematic and layout files.
* ```images``` - Images of my board and the files I printed to do the toner transfer.
* ```test_scripts``` - Some python scripts to test the operation of the board.

## Video

<a href="http://www.youtube.com/watch?feature=player_embedded&v=rbkoJQEUt60" target="_blank"><img src="http://img.youtube.com/vi/rbkoJQEUt60/0.jpg" width="560" height="315" border="10" /></a>

## Thanks

Thanks to the folks on the [Raspberry Pi BB](http://www.raspberrypi.org/phpBB3/viewtopic.php?t=19222), without their guidance it would have taken me longer to figure this out.
