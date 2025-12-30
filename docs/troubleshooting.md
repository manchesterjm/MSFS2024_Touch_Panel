# Troubleshooting Guide

## Common Issues

### 1. Buttons Send Commands But Don't Change Color

**Symptom:** Pressing a button toggles the function in MSFS (e.g., AP turns on/off), but the button color stays yellow.

**Cause:** WASimModule is not installed. The plugin can send commands via SimConnect, but cannot receive state updates without WASimModule.

**Solution:**
1. Download WASimModule from [GitHub releases](https://github.com/mpaperno/MSFSTouchPortalPlugin/releases)
2. Extract `wasimcommander-module` folder to MSFS 2024 Community folder:
   ```
   C:\Users\[username]\AppData\Local\Packages\Microsoft.Limitless_8wekyb3d8bbwe\LocalCache\Packages\Community
   ```
3. **Restart MSFS 2024 completely** (not just reload the flight)

**Verification:**
Check the plugin log at:
```
C:\Users\[username]\AppData\Roaming\TouchPortal\plugins\MSFS-TouchPortal-Plugin\logs\
```

- **Bad:** `WASM Server not found or couldn't connect`
- **Good:** `Connected to WASimModule Server v01030200`

---

### 2. Buttons Don't Do Anything

**Symptom:** Pressing buttons has no effect on MSFS at all.

**Possible Causes:**

#### Touch Portal Not Connected
- Check mobile app shows "Connected"
- Ensure both devices on same network
- Try restarting both apps

#### MSFS Not Running
- Plugin only works when MSFS is running
- Must be in a flight (not main menu)

#### Plugin Not Loaded
- Go to Touch Portal Settings → Plugins
- Verify "MSFS Touch Portal Plugin" is listed and enabled
- If missing, re-import the `.tpp` file

#### SimConnect Issue
- Restart MSFS completely
- Check Windows Firewall isn't blocking SimConnect

---

### 3. Gear Button Shows Wrong State

**Symptom:** Gear button shows red (up) when gear is actually down, or vice versa.

**Explanation:** The Gear state uses `GearTotalExtended` which returns:
- `100` = Fully extended (down)
- `0` = Fully retracted (up)
- Values between = In transit

**Solution:** The button is configured to check for `100` (down) = green, `0` (up) = red. This should work correctly. If not:
1. Verify you're using the correct state ID
2. Check the aircraft actually reports gear state (some aircraft don't)

---

### 4. Only Some Buttons Work

**Symptom:** Some buttons work perfectly, others don't respond.

**Possible Causes:**

#### Aircraft-Specific Features
- Not all aircraft have all features
- Example: Propeller anti-ice doesn't exist on jets
- Example: Some aircraft use different AP modes

#### State ID Mismatch
- Some states are aircraft-dependent
- The Longitude may report states differently than other aircraft

---

### 5. Touch Portal Shows "Plugin Error"

**Symptom:** Red error indicator on plugin.

**Solution:**
1. Go to Touch Portal Settings → Plugins
2. Click on MSFS plugin
3. Click "Restart Plugin"
4. If still failing, check logs in:
   ```
   C:\Users\[username]\AppData\Roaming\TouchPortal\plugins\MSFS-TouchPortal-Plugin\logs\
   ```

---

### 6. Connection Drops During Flight

**Symptom:** Buttons stop working mid-flight.

**Possible Causes:**
- Network connectivity issue between PC and mobile device
- SimConnect disconnect (rare)
- MSFS focus/alt-tab issue

**Solution:**
- Check WiFi connection on mobile device
- Return focus to MSFS
- Restart Touch Portal if needed

---

## Plugin Log Location

```
C:\Users\[username]\AppData\Roaming\TouchPortal\plugins\MSFS-TouchPortal-Plugin\logs\
```

Log files contain:
- Connection status
- State update messages
- Error messages
- Action execution confirmations

---

## Getting Help

1. **Plugin Issues:** [GitHub Issues](https://github.com/mpaperno/MSFSTouchPortalPlugin/issues)
2. **Touch Portal Issues:** [Touch Portal Discord](https://discord.gg/MgxQb8r)
3. **MSFS Issues:** [MSFS Forums](https://forums.flightsimulator.com/)

---

## Diagnostic Checklist

- [ ] Touch Portal Pro license active
- [ ] Plugin imported and enabled
- [ ] WASimModule installed in Community folder
- [ ] MSFS restarted after WASimModule install
- [ ] Both apps on same network
- [ ] Mobile app connected to desktop
- [ ] MSFS running and in a flight
- [ ] Plugin log shows "Connected to WASimModule Server"
