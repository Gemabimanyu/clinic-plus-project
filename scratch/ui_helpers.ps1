Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

Add-Type @"
using System;
using System.Runtime.InteropServices;
public class WinCtl {
  public delegate bool EnumWindowsProc(IntPtr hWnd, IntPtr lParam);
  [DllImport("user32.dll")] public static extern bool EnumWindows(EnumWindowsProc lpEnumFunc, IntPtr lParam);
  [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr hWnd);
  [DllImport("user32.dll")] public static extern uint GetWindowThreadProcessId(IntPtr hWnd, out uint processId);
  [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr hWnd);
  [DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);
  [DllImport("user32.dll")] public static extern bool BringWindowToTop(IntPtr hWnd);
  [DllImport("user32.dll")] public static extern IntPtr GetForegroundWindow();
  public static IntPtr Found = IntPtr.Zero;
  public static void FindByPid(uint targetPid) {
    Found = IntPtr.Zero;
    EnumWindows(new EnumWindowsProc((hWnd, lParam) => {
      if (IsWindowVisible(hWnd)) {
        uint pid; GetWindowThreadProcessId(hWnd, out pid);
        if (pid == targetPid) { Found = hWnd; return false; }
      }
      return true;
    }), IntPtr.Zero);
  }
}
public class SendInputHelper {
  [StructLayout(LayoutKind.Sequential)]
  public struct MOUSEINPUT { public int dx; public int dy; public uint mouseData; public uint dwFlags; public uint time; public IntPtr dwExtraInfo; }
  [StructLayout(LayoutKind.Sequential)]
  public struct KEYBDINPUT { public ushort wVk; public ushort wScan; public uint dwFlags; public uint time; public IntPtr dwExtraInfo; }
  [StructLayout(LayoutKind.Explicit)]
  public struct INPUTUNION { [FieldOffset(0)] public MOUSEINPUT mi; [FieldOffset(0)] public KEYBDINPUT ki; }
  [StructLayout(LayoutKind.Sequential)]
  public struct INPUT { public uint type; public INPUTUNION u; }
  [DllImport("user32.dll")] public static extern uint SendInput(uint nInputs, INPUT[] pInputs, int cbSize);
  [DllImport("user32.dll")] public static extern int GetSystemMetrics(int nIndex);
  public const uint INPUT_MOUSE = 0, INPUT_KEYBOARD = 1;
  public const uint MOUSEEVENTF_MOVE = 0x0001, MOUSEEVENTF_ABSOLUTE = 0x8000, MOUSEEVENTF_LEFTDOWN = 0x0002, MOUSEEVENTF_LEFTUP = 0x0004;
  public const uint KEYEVENTF_KEYUP = 0x0002, KEYEVENTF_UNICODE = 0x0004;

  // Matches Take-Screenshot's Bounds space (2752x1152) directly — a ×1.25
  // "true resolution" correction was tried and empirically made things WORSE
  // (identical wrong landing spot before and after), so don't reintroduce it.
  // There's a real, still-unexplained nonlinearity in aim->landing (~1 row
  // low in this session) — verify every click with a screenshot rather than
  // trusting the formula alone.
  public const int SCREEN_W = 2752, SCREEN_H = 1152;
  public static void ClickAt(int x, int y) {
    int nx = (int)(x * 65535.0 / (SCREEN_W - 1));
    int ny = (int)(y * 65535.0 / (SCREEN_H - 1));
    var move = new INPUT { type = INPUT_MOUSE, u = new INPUTUNION { mi = new MOUSEINPUT { dx = nx, dy = ny, dwFlags = MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE } } };
    SendInput(1, new INPUT[] { move }, Marshal.SizeOf(typeof(INPUT)));
    System.Threading.Thread.Sleep(250);
    var down = new INPUT { type = INPUT_MOUSE, u = new INPUTUNION { mi = new MOUSEINPUT { dx = nx, dy = ny, dwFlags = MOUSEEVENTF_LEFTDOWN | MOUSEEVENTF_ABSOLUTE } } };
    SendInput(1, new INPUT[] { down }, Marshal.SizeOf(typeof(INPUT)));
    System.Threading.Thread.Sleep(150);
    var up = new INPUT { type = INPUT_MOUSE, u = new INPUTUNION { mi = new MOUSEINPUT { dx = nx, dy = ny, dwFlags = MOUSEEVENTF_LEFTUP | MOUSEEVENTF_ABSOLUTE } } };
    SendInput(1, new INPUT[] { up }, Marshal.SizeOf(typeof(INPUT)));
    System.Threading.Thread.Sleep(300);
  }

  [DllImport("user32.dll")] public static extern short VkKeyScan(char ch);
  public static void PressKey(ushort vk) {
    var down = new INPUT { type = INPUT_KEYBOARD, u = new INPUTUNION { ki = new KEYBDINPUT { wVk = vk } } };
    var up = new INPUT { type = INPUT_KEYBOARD, u = new INPUTUNION { ki = new KEYBDINPUT { wVk = vk, dwFlags = KEYEVENTF_KEYUP } } };
    SendInput(1, new INPUT[] { down }, Marshal.SizeOf(typeof(INPUT)));
    System.Threading.Thread.Sleep(80);
    SendInput(1, new INPUT[] { up }, Marshal.SizeOf(typeof(INPUT)));
    System.Threading.Thread.Sleep(150);
  }

  public static void TypeText(string text) {
    foreach (char c in text) {
      var down = new INPUT { type = INPUT_KEYBOARD, u = new INPUTUNION { ki = new KEYBDINPUT { wScan = c, dwFlags = KEYEVENTF_UNICODE } } };
      var up = new INPUT { type = INPUT_KEYBOARD, u = new INPUTUNION { ki = new KEYBDINPUT { wScan = c, dwFlags = KEYEVENTF_UNICODE | KEYEVENTF_KEYUP } } };
      SendInput(1, new INPUT[] { down }, Marshal.SizeOf(typeof(INPUT)));
      System.Threading.Thread.Sleep(30);
      SendInput(1, new INPUT[] { up }, Marshal.SizeOf(typeof(INPUT)));
      System.Threading.Thread.Sleep(40);
    }
  }
}
"@

function Focus-Clinic($targetPid) {
  [WinCtl]::FindByPid($targetPid)
  $hwnd = [WinCtl]::Found
  [WinCtl]::ShowWindow($hwnd, 6) | Out-Null
  Start-Sleep -Milliseconds 250
  [WinCtl]::ShowWindow($hwnd, 9) | Out-Null
  [WinCtl]::BringWindowToTop($hwnd) | Out-Null
  [WinCtl]::SetForegroundWindow($hwnd) | Out-Null
  Start-Sleep -Milliseconds 500
  return $hwnd
}

function Click-At($x, $y) { [SendInputHelper]::ClickAt($x, $y) }
function Type-Text($t) { [SendInputHelper]::TypeText($t) }
function Press-Key($vk) { [SendInputHelper]::PressKey($vk) }
# VK_ESCAPE=0x1B, VK_TAB=0x09, VK_RETURN=0x0D, VK_LEFT=0x25 (Alt+Left = back on many apps)

function Take-Screenshot($path) {
  $bounds = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
  $bmp = New-Object System.Drawing.Bitmap $bounds.Width, $bounds.Height
  $g = [System.Drawing.Graphics]::FromImage($bmp)
  $g.CopyFromScreen($bounds.Location, [System.Drawing.Point]::Empty, $bounds.Size)
  $bmp.Save($path, [System.Drawing.Imaging.ImageFormat]::Png)
  $g.Dispose(); $bmp.Dispose()
}
