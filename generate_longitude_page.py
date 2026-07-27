#!/usr/bin/env python3
"""
Generate a Touch Portal page for MSFS 2024 Citation Longitude
Uses calculator code actions for Longitude-specific controls
"""

import json
import uuid
import time

def generate_id():
    """Generate a unique button ID"""
    return f"u{uuid.uuid4().hex[:12]}"

def create_calc_code_action(code, hold_repeat="Off"):
    """Create an Execute Calculator Code action"""
    return {
        "kPlugType": 2,
        "kmald": json.dumps([{
            "data": [{"lineFormat": f"Execute this code: {code} (must be valid RPN format)"}],
            "language": "default",
            "suggestions": {}
        }]),
        "kID": "MSFSTouchPortalPlugin.Plugin.Action.ExecCalcCode",
        "kPrefix": "MSFS",
        "kInline": "false",
        "kHHF": "true" if hold_repeat == "On" else "false",
        "kcD": -14606047,
        "kPID": "MSFSTouchPortalPlugin",
        "kData": [
            {"id": "MSFSTouchPortalPlugin.Plugin.Action.ExecCalcCode.Data.Code", "type": "text", "label": "Code", "default": code},
            {"id": "MSFSTouchPortalPlugin.Plugin.Action.ExecCalcCode.Data.OnHoldAction", "type": "choice", "label": "On Hold Action", "default": "Press", "valueChoices": ["Press", "Release", "Press & Release", "Repeat Only"]},
            {"id": "MSFSTouchPortalPlugin.Plugin.Action.ExecCalcCode.Data.OnHoldRepeat", "type": "choice", "label": "Repeat While Held", "default": hold_repeat, "valueChoices": ["On", "Off"]},
            {"id": "MSFSTouchPortalPlugin.Plugin.Action.ExecCalcCode.Data.OnHoldRate", "type": "text", "label": "Rate", "default": ""},
            {"id": "MSFSTouchPortalPlugin.Plugin.Action.ExecCalcCode.Data.OnHoldDelay", "type": "text", "label": "Delay", "default": ""}
        ],
        "kVals": [
            {"VAL": code, "ID": "MSFSTouchPortalPlugin.Plugin.Action.ExecCalcCode.Data.Code", "TYPE": "text"},
            {"VAL": "Press", "ID": "MSFSTouchPortalPlugin.Plugin.Action.ExecCalcCode.Data.OnHoldAction", "TYPE": "choice"},
            {"VAL": hold_repeat, "ID": "MSFSTouchPortalPlugin.Plugin.Action.ExecCalcCode.Data.OnHoldRepeat", "TYPE": "choice"},
            {"VAL": "", "ID": "MSFSTouchPortalPlugin.Plugin.Action.ExecCalcCode.Data.OnHoldRate", "TYPE": "text"},
            {"VAL": "", "ID": "MSFSTouchPortalPlugin.Plugin.Action.ExecCalcCode.Data.OnHoldDelay", "TYPE": "text"}
        ],
        "kmold": "",
        "kStatic": "false",
        "kcL": -16740097,
        "kIEn": True,
        "kDesc": "",
        "kET": 0,
        "KEY_TYPE": "PLUGIN_ACTION",
        "kFormat": f"Execute this code: {code} (must be valid RPN format)",
        "kName": "Execute Calculator Code",
        "kpip": ""
    }

def create_state_event(state_id, state_name, value, on_color, off_color=-14145496):
    """Create state change events for button visual feedback"""
    return [
        {
            "KEY_STATE_CACHED_NAME": state_name,
            "KEY_STATE_DESCRIPTION": "On state changes to",
            "kPSC": True,
            "kIEn": True,
            "KEY_IS_NOT_EQUAL": False,
            "kCSC": 0,
            "KEY_STATE": str(value),
            "KEY_STATE_ID": state_id,
            "KEY_TYPE": "ON_STATE_AWARENESS_CHANGE",
            "kICustom": False
        },
        {
            "KEY_IS_CHANGE_IS_FULL_ICON": False,
            "kiTF": False,
            "KEY_START_COLOR": on_color,
            "kiTOV": False,
            "KEY_IS_CHANGE_TITLE": False,
            "KEY_IS_CHANGE_TEXT_COLOR": False,
            "KEY_END_COLOR": -16777216,
            "KEY_IS_CHANGE_ICON": False,
            "kiBD": False,
            "KEY_IS_CHANGE_ALIGN_HOR": False,
            "KEY_IS_CHANGE_IS_ROUNDED": False,
            "kIEn": True,
            "kC": False,
            "kiTOH": False,
            "KEY_TYPE": "CHANGE_BUTTON_VISUALS_ACTION",
            "KEY_IS_CHANGE_BG_COLOR": True,
            "KEY_IS_CHANGE_IS_TRANSPARENT": False,
            "KEY_IS_CHANGE_ALIGN_VERT": False
        }
    ]

def create_button(title, actions, events=None, bg_color=-14145496, text_color=-1):
    """Create a complete button definition"""
    btn = {
        "kSCM": 25,
        "kIAPBKC": -14803426,
        "ITS": True,
        "IiS": False,
        "kSCC": -4611631,
        "id": generate_id(),
        "GUdata": "",
        "kCT": 1,
        "TELS": 5,
        "kSCI": "",
        "kIAs": [],
        "GUid": -1,
        "kSVP": 0,
        "kSVAC": -10575407,
        "inB": False,
        "kSCTM": 0,
        "inC": 0,
        "FF": "Default",
        "A": actions if isinstance(actions, list) else [actions],
        "kMB": 0,
        "kWvZ": 1,
        "BD": 1,
        "C": [],
        "BE": -16777216,
        "BG": bg_color,
        "E": events or [],
        "I": "",
        "BiR": True,
        "kSCTY": 0,
        "kML": 0,
        "BiT": False,
        "kSCHS": False,
        "inS": "",
        "kMR": 0,
        "kMT": 0,
        "T": title,
        "kSCAC": bg_color,
        "kSCHRC": False,
        "THO": 4,
        "kWvU": "",
        "kSCIUFATS": False,
        "kSIP": 0,
        "Ialt": "",
        "kSCIIVA": True,
        "COLS": 1,
        "TA": 5,
        "TC": text_color,
        "kSTP": 0,
        "TO": 4,
        "TP": 2,
        "kSD": 0,
        "TS": -1,
        "ROWS": 1
    }
    return btn

def create_empty_button():
    """Create an empty placeholder button"""
    return {
        "kSCM": 25,
        "kIAPBKC": -14803426,
        "ITS": True,
        "IiS": False,
        "kSCC": -4611631,
        "id": generate_id(),
        "GUdata": "",
        "kCT": 1,
        "TELS": 5,
        "kSCI": "",
        "kIAs": [],
        "GUid": -1,
        "kSVP": 0,
        "kSVAC": -10575407,
        "inB": False,
        "kSCTM": 0,
        "inC": 0,
        "FF": "Default",
        "A": [],
        "kMB": 0,
        "kWvZ": 1,
        "BD": 1,
        "C": [],
        "BE": -16777216,
        "BG": -15000805,  # Dark gray
        "E": [],
        "I": "",
        "BiR": True,
        "kSCTY": 0,
        "kML": 0,
        "BiT": False,
        "kSCHS": False,
        "inS": "",
        "kMR": 0,
        "kMT": 0,
        "T": "",
        "kSCAC": -15000805,
        "kSCHRC": False,
        "THO": 4,
        "kWvU": "",
        "kSCIUFATS": False,
        "kSIP": 0,
        "Ialt": "",
        "kSCIIVA": True,
        "COLS": 1,
        "TA": 5,
        "TC": -1,
        "kSTP": 0,
        "TO": 4,
        "TP": 2,
        "kSD": 0,
        "TS": -1,
        "ROWS": 1
    }

# Color constants (signed 32-bit int)
GREEN = -16711936   # 0xFF00FF00
RED = -65536        # 0xFFFF0000
YELLOW = -256       # 0xFFFFFF00
CYAN = -16711681    # 0xFF00FFFF
BLUE = -16776961    # 0xFF0000FF
ORANGE = -32768     # 0xFFFF8000
DARK_GRAY = -15000805
DEFAULT_BG = -14145496

# Define Longitude-specific buttons
LONGITUDE_BUTTONS = {
    # Row 1: Autopilot Master Controls
    "row1": [
        {"title": "AP", "code": "(>K:AP_MASTER)", "state_id": "MSFSTouchPortalPlugin.AutoPilot.State.AutoPilotMaster", "state_name": "MSFS - AutoPilot - AutoPilot Master Status"},
        {"title": "FD", "code": "(>K:TOGGLE_FLIGHT_DIRECTOR)", "state_id": "MSFSTouchPortalPlugin.AutoPilot.State.AutoPilotFlightDirector", "state_name": "MSFS - AutoPilot - Flight Director Status"},
        {"title": "A/T", "code": "(>K:AUTO_THROTTLE_ARM)", "state_id": "MSFSTouchPortalPlugin.AutoPilot.State.AutoThrottleArm", "state_name": "MSFS - AutoPilot - Auto Throttle Arm"},
        {"title": "YD", "code": "(>K:YAW_DAMPER_TOGGLE)", "state_id": "MSFSTouchPortalPlugin.AutoPilot.State.YawDamper", "state_name": "MSFS - AutoPilot - Yaw Damper Status"},
        {"title": "VNAV", "code": "(L:XMLVAR_VNAVButtonValue) ! (>L:XMLVAR_VNAVButtonValue)", "lvar_state": True},
    ],

    # Row 2: Lateral Modes
    "row2": [
        {"title": "HDG", "code": "(>K:AP_HDG_HOLD)", "state_id": "MSFSTouchPortalPlugin.AutoPilot.State.AutoPilotHeadingHold", "state_name": "MSFS - AutoPilot - Heading Hold Status"},
        {"title": "NAV", "code": "(>K:AP_NAV1_HOLD)", "state_id": "MSFSTouchPortalPlugin.AutoPilot.State.AutoPilotNav1Hold", "state_name": "MSFS - AutoPilot - Nav1 Lock Status"},
        {"title": "APR", "code": "(>K:AP_APR_HOLD)", "state_id": "MSFSTouchPortalPlugin.AutoPilot.State.AutoPilotApproachHold", "state_name": "MSFS - AutoPilot - Approach Hold Status"},
        {"title": "BC", "code": "(>K:AP_BC_HOLD)", "state_id": "MSFSTouchPortalPlugin.AutoPilot.State.AutoPilotBackCourse", "state_name": "MSFS - AutoPilot - Back Course Status"},
        {"title": "HDG\nSYNC", "code": "(A:HEADING INDICATOR, degrees) (>K:HEADING_BUG_SET)"},
    ],

    # Row 3: Vertical Modes
    "row3": [
        {"title": "ALT", "code": "(>K:AP_ALT_HOLD)", "state_id": "MSFSTouchPortalPlugin.AutoPilot.State.AutoPilotAltitudeLock", "state_name": "MSFS - AutoPilot - Altitude Lock Status"},
        {"title": "VS", "code": "(>K:AP_PANEL_VS_HOLD)", "state_id": "MSFSTouchPortalPlugin.AutoPilot.State.AutoPilotVerticalSpeedHold", "state_name": "MSFS - AutoPilot - Vertical Speed Hold Status"},
        {"title": "FLC", "code": "(>K:FLIGHT_LEVEL_CHANGE) (A:AIRSPEED INDICATED, knots) (>K:AP_SPD_VAR_SET)", "state_id": "MSFSTouchPortalPlugin.AutoPilot.State.AutoPilotFlightLevelChange", "state_name": "MSFS - AutoPilot - Flight Level Change Status"},
        {"title": "SPD\nMAN", "code": "1 (>L:XMLVAR_SpeedIsManuallySet)", "lvar_state": True},
        {"title": "SPD\nFMS", "code": "0 (>L:XMLVAR_SpeedIsManuallySet)", "lvar_state": True},
    ],

    # Row 4: Adjustments (with hold-repeat for knobs)
    "row4": [
        {"title": "HDG\n-", "code": "1 (>K:HEADING_BUG_DEC)", "hold": True},
        {"title": "HDG\n+", "code": "1 (>K:HEADING_BUG_INC)", "hold": True},
        {"title": "ALT\n-100", "code": "100 (>K:AP_ALT_VAR_DEC)", "hold": True},
        {"title": "ALT\n+100", "code": "100 (>K:AP_ALT_VAR_INC)", "hold": True},
        {"title": "ALT\n-1000", "code": "1000 (>K:AP_ALT_VAR_DEC)"},
    ],

    # Row 5: More adjustments
    "row5": [
        {"title": "ALT\n+1000", "code": "1000 (>K:AP_ALT_VAR_INC)"},
        {"title": "VS\n-", "code": "(>K:AP_VS_VAR_DEC)", "hold": True},
        {"title": "VS\n+", "code": "(>K:AP_VS_VAR_INC)", "hold": True},
        {"title": "SPD\n-", "code": "1 (>B:AUTOPILOT_SPEED_Dec)", "hold": True},
        {"title": "SPD\n+", "code": "1 (>B:AUTOPILOT_SPEED_Inc)", "hold": True},
    ],

    # Row 6: Baro and Mach
    "row6": [
        {"title": "BARO\n-", "code": "0 (>K:KOHLSMAN_DEC)", "hold": True},
        {"title": "BARO\n+", "code": "0 (>K:KOHLSMAN_INC)", "hold": True},
        {"title": "BARO\nSTD", "code": "(>K:BAROMETRIC_STD_PRESSURE)"},
        {"title": "MACH\nTOG", "code": "(>K:AP_MANAGED_SPEED_IN_MACH_TOGGLE) (A:AUTOPILOT MANAGED SPEED IN MACH, Bool) (>L:XMLVAR_AirSpeedIsInMach)"},
        {"title": "", "empty": True},
    ],
}

def generate_page():
    """Generate the complete Touch Portal page"""

    rows = []
    columns = 5

    for row_key in ["row1", "row2", "row3", "row4", "row5", "row6"]:
        row_buttons = []
        row_data = LONGITUDE_BUTTONS.get(row_key, [])

        for btn_def in row_data:
            if btn_def.get("empty"):
                row_buttons.append(create_empty_button())
            else:
                # Create action
                hold = "On" if btn_def.get("hold") else "Off"
                action = create_calc_code_action(btn_def["code"], hold)

                # Create events for state feedback if state_id is provided
                events = []
                if "state_id" in btn_def:
                    # State = 1 -> Green
                    events.extend(create_state_event(
                        btn_def["state_id"],
                        btn_def["state_name"],
                        "1",
                        GREEN
                    ))
                    # State = 0 -> Default
                    events.extend(create_state_event(
                        btn_def["state_id"],
                        btn_def["state_name"],
                        "0",
                        DEFAULT_BG
                    ))

                row_buttons.append(create_button(
                    btn_def["title"],
                    action,
                    events if events else None,
                    bg_color=YELLOW if "+" in btn_def["title"] or "-" in btn_def["title"] else DEFAULT_BG
                ))

        # Pad row to column count
        while len(row_buttons) < columns:
            row_buttons.append(create_empty_button())

        rows.append(row_buttons)

    # Create page structure
    page = {
        "kATO": "",
        "BG": DEFAULT_BG,
        "MAX": False,
        "BGI": "",
        "kPL": 0,
        "kGB": False,
        "GUid": -1,
        "KEY_ID": str(int(time.time() * 1000)),
        "kATY": 0,
        "BUTTONS": rows,
        "KEY_COLUMNS": columns,
        "kFM": 0,
        "kBN": 0,
        "VERSION": 4,
        "kENA": True,
        "GUdata": "",
        "KEY_TITLE": "Citation Longitude",
        "KEY_ROWS": len(rows),
        "BTN_MARGIN": 0,
        "PO": 0
    }

    return page


if __name__ == "__main__":
    page = generate_page()

    output_path = "/mnt/d/Projects/MSFS2024_Touch_Panel/Citation_Longitude.tml"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(page, f, ensure_ascii=False)

    print(f"Generated: {output_path}")
    print(f"Rows: {len(page['BUTTONS'])}, Columns: {page['KEY_COLUMNS']}")
    print(f"Total buttons: {sum(len(row) for row in page['BUTTONS'])}")
