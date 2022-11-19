# ToBoo

The virtual pet todo app for the command line!

## Description

*ToBoo* is a CLI todo app all about raising virtual pets. You assign yourself tasks to complete by certain dates/times and help/hurt your pet by completing of forgetting to complete them.

## Usage

*TODO: CLI usage and command-line flags here*

### Playing

When you choose a pet, it starts in its smallest form. Each pet has three stats:

* **exp** - Experience Points
* **hp** - Health Points
* **mp** - Momentum Points

It starts with 0 **exp** and its maximum **hp**. **mp** will reset to 1 at the beginning of each day.

#### Experience Points (*EXP*)

**exp** is about tracking your (and your pet's) overall growth. Each time you complete a task, the **exp** raises by a certain amount. **exp** never decreases.

As you gain large amounts of **exp**, your pet can evolve into new forms. Each pet has its own evolution rate.

#### Health Points (*HP*)

**hp** is about not missing tasks, and getting back on track quickly whenever you do miss one. It is based around the motto of "*never miss twice*", meaning that whenever you drop the ball on a task, don't use it as an excuse for the next one. When you complete all tasks due in a day, your pet heals a small amount. Whenever you miss a task, your **hp** goes down by a small amount. Should it hit 0, ~~your pet will be added to your hall of legacy (NOT IMPLEMENTED YET) and~~ you will need to choose a new pet.

#### Momentum Points (*MP*)

**mp** is about rewarding good habit-making skills. When you complete multiple tasks in a row without missing, you gain **mp**. Each time you gain **exp** for completing a task, your **mp** factors in and helps you "level up" even faster! When you miss a task, you **mp** resets back to 1.

#### Mood

You pet will shown a specific mood depending on it's **hp** and **mp**.

* Pets appear *sad* when you're not doing so great, with very low **hp** or **mp**, or both.
* Pets appear *neutral* when they're doing ok but could be better, like when you have high **hp** but low **mp**.
* Pets appear *happy* when you're doing awesome and they have high **hp** and **mp**.
* ~~Some pets can also appear *very happy* when you've crushed it and completed everything due that day. (NOT IMPLEMENTED YET)~~

## License

MIT License
