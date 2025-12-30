# MSFS 2024 Touch Portal Control Panel

A Touch Portal Pro configuration for controlling Microsoft Flight Simulator 2024, specifically designed for the **Cessna Citation Longitude (C700)**.

## Overview

This project provides a complete Touch Portal page with buttons for autopilot, lights, flight systems, and anti-ice controls. All buttons feature **state-based color feedback** (green = ON, red = OFF) using SimConnect integration.

## Screenshots

*(Add screenshots of your Touch Portal page here)*

## Requirements

### Software
- **Touch Portal Pro** - $12.99 one-time purchase ([touch-portal.com](https://www.touch-portal.com/))
- **MSFS Touch Portal Plugin** v1.6.0+ ([GitHub](https://github.com/mpaperno/MSFSTouchPortalPlugin) | [flightsim.to](https://flightsim.to/file/36546/msfs-touch-portal-plugin))
- **WASimModule** - REQUIRED for state feedback ([GitHub releases](https://github.com/mpaperno/MSFSTouchPortalPlugin/releases))
- **Microsoft Flight Simulator 2024**

### Hardware
- Android or iOS device running Touch Portal mobile app
- PC running Touch Portal desktop app
- Both on same network

## Installation

### 1. Install Touch Portal Pro
1. Download Touch Portal from [touch-portal.com](https://www.touch-portal.com/)
2. Install desktop app on PC
3. Install mobile app on phone/tablet
4. Purchase Pro upgrade ($12.99) via mobile app
5. Restart desktop app to recognize Pro license

### 2. Install MSFS Touch Portal Plugin
1. Download latest release from [GitHub](https://github.com/mpaperno/MSFSTouchPortalPlugin/releases)
2. In Touch Portal: Settings tab → Import plug-in
3. Select the downloaded `.tpp` file
4. Restart Touch Portal

### 3. Install WASimModule (CRITICAL)
**Without WASimModule, buttons can send commands but won't receive state updates (colors won't change).**

1. Download `wasimcommander-module` from [GitHub releases](https://github.com/mpaperno/MSFSTouchPortalPlugin/releases)
2. Extract to MSFS 2024 Community folder:
   ```
   C:\Users\[username]\AppData\Local\Packages\Microsoft.Limitless_8wekyb3d8bbwe\LocalCache\Packages\Community
   ```
3. **Restart MSFS 2024 completely**

### 4. Import Touch Portal Page
1. Copy `(main).tml` to:
   ```
   C:\Users\[username]\AppData\Roaming\TouchPortal\pages\
   ```
2. Restart Touch Portal
3. The page should appear automatically

## Button Layout

### Row 1 - Primary Autopilot
| Button | Function | State |
|--------|----------|-------|
| **AP** | Autopilot Master | AutoPilotMaster |
| **FD** | Flight Director | AutoPilotFlightDirector |
| **HDG** | Heading Hold | AutoPilotHeadingHold |
| **NAV** | Nav1 Hold | AutoPilotNav1Hold |

### Row 2 - Autopilot Modes
| Button | Function | State |
|--------|----------|-------|
| **ALT** | Altitude Hold | AutoPilotAltitudeHold |
| **VS** | Vertical Speed | AutoPilotVerticalSpeedHold |
| **APR** | Approach Mode | AutoPilotApproachHold |
| **FLC** | Flight Level Change | AutoPilotFlightLevelChange |

### Row 3 - Flight Systems
| Button | Function | State |
|--------|----------|-------|
| **LAND** | Landing Lights | LandingLight |
| **GEAR** | Gear Toggle | GearTotalExtended (100=down, 0=up) |
| **BRK** | Parking Brake | ParkingBrake |
| **SPLR** | Spoilers Arm | SpoilersArmed |

### Row 4 - Exterior Lights
| Button | Function | State |
|--------|----------|-------|
| **NAV LT** | Navigation Lights | NavigationLight |
| **STRB** | Strobe Lights | StrobeLight |
| **BCN** | Beacon | BeaconLight |
| **TAXI** | Taxi Lights | TaxiLight |

### Row 5 - Anti-Ice & More AP
| Button | Function | State |
|--------|----------|-------|
| **PITOT** | Pitot Heat | PitotHeat |
| **YD** | Yaw Dampener | AutoPilotYawDampener |
| **LOC** | Localizer | AutoPilotLocalizerHold |
| **BC** | Back Course | AutoPilotBackCourseHold |

### Row 6 - Anti-Ice Systems
| Button | Function | State |
|--------|----------|-------|
| **STRC** | Structural De-Ice | StructuralDeIce |
| **ENG1** | Engine 1 Anti-Ice | Engine1AntiIce |
| **ENG2** | Engine 2 Anti-Ice | Engine2AntiIce |
| **ATT** | Attitude Hold | AutoPilotAttitudeHold |

### Row 7 - Additional Autopilot Modes
| Button | Function | State |
|--------|----------|-------|
| **MACH** | Mach Hold | AutoPilotMachHold |
| **N1** | N1 Hold | AutoPilotN1Hold |
| **WLVL** | Wing Leveler | AutoPilotWingLeveler |
| **BANK** | Bank Mode | AutoPilotBankMode |

### Row 8 - Flaps Control
| Button | Function | Notes |
|--------|----------|-------|
| **FLP UP** | Flaps Full Up | No state feedback |
| **FLP DN** | Flaps Full Down | No state feedback |
| **FLP +** | Flaps Increase | Incremental |
| **FLP -** | Flaps Decrease | Incremental |

### Row 9 - Trim Controls
| Button | Function | Notes |
|--------|----------|-------|
| **TRIM UP** | Elevator Trim Up | No state feedback |
| **TRIM DN** | Elevator Trim Down | No state feedback |
| **AIL L** | Aileron Trim Left | No state feedback |
| **AIL R** | Aileron Trim Right | No state feedback |

## Color Codes

| Color | Hex | Decimal | Meaning |
|-------|-----|---------|---------|
| Green | #00FF00 | -16711936 | ON/Active |
| Red | #FF0000 | -65536 | OFF/Inactive |
| Yellow | #FFFF00 | -256 | Default/Unknown |
| Gray | #CCCCCC | -3355444 | No state feedback (action only) |

## File Structure

```
MSFS2024_Touch_Panel/
├── README.md                 # This file
├── (main).tml               # Touch Portal page configuration
├── docs/
│   └── troubleshooting.md   # Common issues and solutions
└── screenshots/             # UI screenshots
```

## How Buttons Work

Each button has two main components:

### Action (On Pressed)
Sends a command to MSFS via SimConnect:
```json
{
  "kID": "MSFSTouchPortalPlugin.AutoPilot.Action.AutoPilotSwitches",
  "kVals": [
    {"VAL": "Master", "ID": "...Data.0"},
    {"VAL": "Toggle", "ID": "...Data.1"}
  ]
}
```

### Events (State Changes)
Monitors SimConnect state and changes button color:
```json
{
  "KEY_STATE_ID": "MSFSTouchPortalPlugin.AutoPilot.State.AutoPilotMaster",
  "KEY_STATE": "1",  // When state equals 1
  "KEY_TYPE": "ON_STATE_AWARENESS_CHANGE"
},
{
  "KEY_START_COLOR": -16711936,  // Change to green
  "KEY_TYPE": "CHANGE_BUTTON_VISUALS_ACTION"
}
```

## Troubleshooting

### Buttons don't change color
1. **Check WASimModule is installed** - Most common issue
2. Check plugin log: `C:\Users\[username]\AppData\Roaming\TouchPortal\plugins\MSFS-TouchPortal-Plugin\logs\`
3. Look for: `WASM Server not found or couldn't connect` → WASimModule not installed
4. Look for: `Connected to WASimModule Server v01030200` → Working correctly

### Buttons don't do anything
1. Verify Touch Portal is connected to mobile app
2. Verify MSFS is running
3. Check plugin is loaded (should show in Touch Portal plugin list)
4. Try restarting both Touch Portal and MSFS

### Wrong aircraft states
- Some states are aircraft-specific
- This page is optimized for Citation Longitude
- May need adjustments for other aircraft

## Future Enhancements

- [x] ~~Row 7 buttons (Mach Hold, N1 Hold, Wing Leveler, Bank Mode)~~
- [x] ~~Flaps increment/decrement buttons~~
- [x] ~~Trim controls~~
- [ ] Rudder trim controls (Row 10)
- [ ] Radio/COM frequency displays
- [ ] Aircraft-specific profiles
- [ ] Speed/altitude value displays

## Technical Reference

### Plugin Action/State IDs

| Category | Action Base | State Base |
|----------|-------------|------------|
| AutoPilot | `MSFSTouchPortalPlugin.AutoPilot.Action.*` | `MSFSTouchPortalPlugin.AutoPilot.State.*` |
| FlightSystems | `MSFSTouchPortalPlugin.FlightSystems.Action.*` | `MSFSTouchPortalPlugin.FlightSystems.State.*` |
| LightSwitches | `MSFSTouchPortalPlugin.LightSwitches.Action.*` | `MSFSTouchPortalPlugin.LightSwitches.State.*` |

### Common Actions

| Action ID | Purpose |
|-----------|---------|
| `AutoPilotSwitches` | Toggle AP modes (Master, HDG, ALT, etc.) |
| `AutoPilotFlightDirectorSwitches` | Flight Director control |
| `LightSwitch` | Toggle various lights |
| `GearManipulate` | Gear up/down/toggle |
| `ParkingBreakToggle` | Parking brake |
| `SpoilersArmToggle` | Arm/disarm spoilers |
| `AntiIceAdjust` | Anti-ice systems |

## Credits

- **MSFS Touch Portal Plugin** by [Max Paperno](https://github.com/mpaperno)
- **Touch Portal** by [Touch Portal](https://www.touch-portal.com/)
- **Configuration** by manchesterjm

## License

This configuration is provided as-is for personal use. Feel free to modify and share.

---

*Last updated: 2025-12-30 - Added Rows 6-9 (Anti-Ice, Additional AP, Flaps, Trim)*
