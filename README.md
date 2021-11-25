# Generate-IL-program-TM221-Schneider
Program that generates code in IL format for Schneider TM221 programmable controllers.  It implements autonomous calendars in the PLC, programmable by modbus through user-defined functions.

The work carried out for the implicit programming of calendars for Schneider TM221 PLC automatons is described.

A calendar for a specific variable needs to use 100MW (words) of the PLC for its programming.

The coding of the words is shown in the following table:

| bit | Description | |
| ------ | ------ |
| 0 | Enabling, days Integer [1-7]|
| [1-12] | MONDAY, 6 timeslots, BCD | [13-24] | TUESDAY, 6 timeslots, BCD |
| [13-24] | TUESDAY, 6 time slots, BCD | [25-36] | [25-36] | TUESDAY, 6 time slots, BCD |
| [25-36] | WEDNESDAY, 6 time slots, BCD | [37-48] | WEDNESDAY, 6 time slots, BCD | [37-48
| [37-48] | THURSDAY, 6 hourly intervals, BCD | [49-60] | THURSDAY, 6 hourly intervals, BCD|
| [49-60] | FRIDAY, 6 time slots, BCD| [49-60] | FRIDAY, 6 time slots, BCD|
| [61-72] | SATURDAY, 6 time slots, BCD| [73-84] | SUNDAY, 6 time slots, BCD|
| [73-84] | SUNDAY, 6 time slots, BCD| [73-84] | [73-84] | SUNDAY, 6 time slots, BCD|
| [85] | [85] | [85] | [85] | Activation bit |

Each circuit to be controlled by calendar requires 7 user-defined function blocks that are placed in a corresponding Task/Rung:

The enable bit attacks the input of the block and the enable bit attacks the output of the module.

Each defined function block follows the following structure:

**1.** Bit enable

**2.** Weekday correspondence

**3.** Time interval 

**4.** Activation signal 

**1. Bit enable**

The enable bit is a calendar enable signal given by the SCADA to enable a corresponding calendar.

**2. Weekday correspondence**

If a corresponding calendar is enabled for a day of the week, the intervals that are configured must only act for the specific day, therefore a check is defined for the corresponding day.

**3. Time interval**

Each day of the week has 6 time slots reserved to define the time range in which the output will be active.

**4. Activation signal**

The activation signal picks up the signal sent by the calendars that will attack each of the circuits.

Depending on the logic followed in the automaton for the activation and deactivation of the circuits, the activation signal is used for this task, in our case a rising edge will send an activation signal, and a falling edge a deactivation signal.

**Automation programming PLC code**

To this end, each line of the program now has a specific row associated with it and the user can modify the code more quickly.

To make programming more efficient, a Python script has been created which, by means of a reference MW, generates a text file with the corresponding lines to be pasted into the program, speeding up the creation and updating of the different function blocks.

| File | Description |
| ------ | ------ |
| gen_program.py | Script |
| plantilla.txt | Reference template |
| programa_dia_x_reg_x.txt | Generated Program |

To run the file you use the Windows console or an anaconda environment where Python is installed.

You select the number of the base reference word.

The program displays the generated code, also available in the file "program_dia_x_reg_x".

Once the text file has been opened with notepad, the user must copy and paste the corresponding lines in (IL) format into the PLC program.
