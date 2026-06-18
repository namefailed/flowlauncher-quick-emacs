# Flow Launcher Quick Emacs

Single repo, two standalone Flow Launcher plugins for Emacs capture:

| Plugin | Keyword | What it does |
|--------|---------|-------------|
| **Quick Journal** | `j` | Appends text to today's **Log** section |
| **Quick Task** | `t` | Inserts a `***** TODO` heading in today's **Tasks** |

Each plugin is a fully self-contained directory — copy it directly to
`%APPDATA%\FlowLauncher\Plugins\` and restart.

## Prerequisites

- [Flow Launcher](https://flowlauncher.com/)
- [Emacs](https://www.gnu.org/software/emacs/) with a running daemon (`emacs --daemon`)
- `emacsclientw` on `PATH`
- The Elisp functions below in your Emacs config

## Installation

```powershell
cd "$env:APPDATA\FlowLauncher\Plugins"

# Quick Journal
Copy-Item -Recurse "path\to\repo\journal" "QuickJournal-1.0.0"

# Quick Task
Copy-Item -Recurse "path\to\repo\task" "QuickTask-1.0.0"
```

Restart Flow Launcher.

## Usage

```
j buy milk       → appends - [2026-06-17 Tue 22:00] buy milk to the Log
t fix auth bug   → inserts ***** TODO fix auth bug in Tasks
```

## Emacs setup

Add these to your Emacs config (tailored for the org-journal file at
`my/org-journal-file` — adjust to your own path):

```elisp
(defun my/flowlauncher-insert-transcript (transcript)
  "Insert TRANSCRIPT into today's journal Log section.
Called from Quick Journal Flow Launcher plugin."
  (let ((ts (format-time-string "- [%Y-%m-%d %a %H:%M] ")))
    (require 'org-datetree)
    (find-file "~/journal.org")
    (org-datetree-find-date-create (calendar-current-date))
    (end-of-line)
    (newline)
    (insert ts transcript)
    (save-buffer)))

(defun my/flowlauncher-insert-task (text)
  "Insert a TODO task from TEXT into today's journal Tasks.
Called from Quick Task Flow Launcher plugin."
  (require 'org-datetree)
  (find-file "~/journal.org")
  (org-datetree-find-date-create (calendar-current-date))
  (end-of-line)
  (insert (concat "\n***** TODO " text))
  (save-buffer))
```

## File structure

```
flowlauncher-quick-emacs/
├── journal/                → Quick Journal plugin (keyword j)
│   ├── plugin.json
│   ├── run.py
│   └── Images/
│       └── journal.png
├── task/                   → Quick Task plugin (keyword t)
│   ├── plugin.json
│   ├── run.py
│   └── Images/
│       └── task.png
├── LICENSE
└── README.md
```

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| "emacsclientw not found" | Add Emacs `bin/` to `PATH` |
| "Symbol's function definition is void" | Load `my/flowlauncher-insert-transcript` / `my/flowlauncher-insert-task` in Emacs config |
| Plugin not showing up | Verify directory is directly under `Plugins\`, restart Flow Launcher |

## License

MIT
