# CLI Bridge Example

The "cliBridge_config.py" script demonstrates bare-bones access to the FreeWave CLI using the **cliBridge** program. **cliBridge** is normally used interactively to access the FreeWave CLI from the Linux Bash shell, but it can also be used programmatically to read or change device configuration.

## Usage

```python cliBridge_config.py```

The program will display a menu of feature to demonstrate. It will run the selected demonstration and then exit.

Note that this program must be run on the ZumLink IPR from the developer environment, since it relies on running the **cliBridge** command directly in a new process.
