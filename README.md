# Raspberry Pi Relay Module Interface Board

## Note / Warning

This was formerly stated to be for the SainSmart relay modules, but it was later pointed out to me that these boards actually already have this logic built in to them. 

## Overview

These interface boards will allow you to connect your [Raspberry Pi](http://www.amazon.com/gp/product/B009SQQF9C/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B009SQQF9C&linkCode=as2&tag=fixedd-20) (rev 2.0, at least) to a 4 or 8-Channel 5V Relay Module.

## Parts List
### 8-Channel 5V Relay Module

| Quantity | Part                             | Notes |
| :------: | -------------------------------- | ----- |
| 8        | 12kΩ ¼ Watt Resistors            | [This multi-pack](http://www.amazon.com/gp/product/B003UC4FSS/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B003UC4FSS&linkCode=as2&tag=fixedd-20) has all the resistors you'll need for this, and much more. |
| 8        | 10kΩ ¼ Watt Resistors            |       |
| 8        | 2N3904 Transistors               | [Amazon](http://www.amazon.com/gp/product/B00AUEFGU0/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00AUEFGU0&linkCode=as2&tag=fixedd-20). |
| 1        | 2 inch x 2 inch single-sided PCB | I cut [this](http://www.amazon.com/gp/product/B000P7ALZC/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B000P7ALZC&linkCode=as2&tag=fixedd-20) down. |
| 1        | 3 inch jumper wire               |       |
| 1        | 26 pin header (2x13)             | [This] will be more than enough. |
| 1        | 10 pin header (1x10)             |       |

### 4-Channel 5V Relay Module
| Quantity | Part                             | Notes |
| :------: | -------------------------------- | ----- |
| 4        | 12kΩ ¼ Watt Resistors            | [This multi-pack](http://www.amazon.com/gp/product/B003UC4FSS/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B003UC4FSS&linkCode=as2&tag=fixedd-20) has all the resistors you'll need for this, and much more. |
| 4        | 10kΩ ¼ Watt Resistors            |       |
| 4        | 2N3904 Transistors               | [Amazon](http://www.amazon.com/gp/product/B00AUEFGU0/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00AUEFGU0&linkCode=as2&tag=fixedd-20). |
| 1        | 2 inch x 2 inch single-sided PCB | I cut [this](http://www.amazon.com/gp/product/B000P7ALZC/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B000P7ALZC&linkCode=as2&tag=fixedd-20) down. |
| 1        | 3 inch jumper wire               |       |
| 1        | 26 pin header (2x13)             | [This] will be more than enough. |
| 1        | 10 pin header (1x10)             |       |

## Explanation

The relay boards are powered by 5v and the relays are triggered by taking the input pin to ground. Since the Raspberry Pi's GPIO pins output 3.3v I used a set of transistors to take the relay pins to ground.

I used 2N3904 transistors simply because they were cheap and readily available. In theory any NPN transistor should work, but the resistors may need to be adjusted.

To make the board I used the toner transfer method. There are [plenty of instructions](http://www.instructables.com/id/Cheap-and-Easy-Toner-Transfer-for-PCB-Making/) on the internet for this, so I won't go into it here.

The Relay Module I used has opto-isolation on the input pins. To maintain this isolation you would need to use an external 5v power supply instead of using the Pi's.

### Files

* ```eagle_files``` - Provided here are [Eagle PCB](http://www.cadsoftusa.com/eagle-pcb-design-software/) schematic and layout files.
* ```gerber_files``` - these are [Gerber format](http://en.wikipedia.org/wiki/Gerber_format) files so it will be easy to have boards manufactured.
* ```images``` - Images of my board and the files I printed to do the toner transfer.
* ```test_scripts``` - Some python scripts to test the operation of the board.

## Video

<a href="http://www.youtube.com/watch?feature=player_embedded&v=rbkoJQEUt60" target="_blank"><img src="http://img.youtube.com/vi/rbkoJQEUt60/0.jpg" width="560" height="315" border="10" /></a>

## Thanks

* Thanks to the folks on the [Raspberry Pi BB](http://www.raspberrypi.org/phpBB3/viewtopic.php?t=19222), without their guidance it would have taken me longer to figure this out.
* Thanks to @lazylester for the Gerber files for the 8-channel version.
* Thanks to @fjung for the Eagle and Gerber files for the 4-channel version.

## License

There is no license other than to say that I release this to the public domain... do with it as you wish (see [the license file](./LICENSE.md)).
