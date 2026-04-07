"""
Daily Job Alert Dashboard — Manual Testing & Playwright JavaScript
Author : PARTHA PATTANAYAK
Python Desktop App using Tkinter (no extra installs required)
Run   : python job_alert_dashboard.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
from datetime import datetime

# ─── DATA ────────────────────────────────────────────────────────────────────

MANUAL_JOBS = [
    {"title": "Manual QA Tester", "company": "Frndly TV", "location": "Remote (US)",
     "skills": ["Manual Testing", "iOS/Android", "Streaming QA", "Regression"],
     "link": "https://www.indeed.com/q-manual-tester-jobs.html", "source": "Indeed", "age": "2h ago"},
    {"title": "QA Engineer (Manual)", "company": "Interviews Chat", "location": "Remote (Global)",
     "skills": ["Manual Testing", "Chrome Extensions", "Mobile Testing", "Desktop Apps"],
     "link": "https://weworkremotely.com/remote-jobs/interviews-chat-qa-engineer", "source": "WeWorkRemotely", "age": "5h ago"},
    {"title": "Manual Test Engineer", "company": "Leidos", "location": "Annapolis Junction, MD",
     "skills": ["System Testing", "Integration Testing", "Security Clearance", "Manual QA"],
     "link": "https://www.indeed.com/q-Manual-Software-Test-Engineer-jobs.html", "source": "Indeed", "age": "8h ago"},
    {"title": "Junior Manual Tester", "company": "NonStop io Technologies", "location": "Remote (India)",
     "skills": ["Manual Testing", "Test Cases", "QA Fundamentals", "Fresher OK"],
     "link": "https://cutshort.io/jobs/manual-testing-jobs", "source": "CutShort", "age": "10h ago"},
    {"title": "QA Engineer (Manual+Auto)", "company": "CloudGeometry", "location": "Remote",
     "skills": ["Manual QA", "API Testing", "Test Plans", "Mobile Testing"],
     "link": "https://www.indeed.com/q-manual-testing-l-remote-jobs.html", "source": "Indeed", "age": "14h ago"},
    {"title": "Software Test Engineer", "company": "Mundrisoft Solution", "location": "Remote",
     "skills": ["Black-box Testing", "Functional Testing", "Regression", "UI Testing"],
     "link": "https://www.indeed.com/q-playwright-testing-l-remote-jobs.html", "source": "Indeed", "age": "18h ago"},
    {"title": "QA Tester", "company": "Town Fair Tire", "location": "Hybrid (US)",
     "skills": ["Manual Testing", "UAT", "SQL", "Jira", "Agile/Scrum"],
     "link": "https://www.dice.com/jobs/q-software+testing-jobs", "source": "Dice", "age": "22h ago"},
]

PLAYWRIGHT_JOBS = [
    {"title": "QA Engineer (Playwright/JS)", "company": "Close CRM", "location": "Remote (USA)",
     "skills": ["Playwright", "Cypress", "JavaScript", "GraphQL", "React Testing Library"],
     "link": "https://weworkremotely.com/listings/close-qa-engineer-usa-only-100-remote", "source": "WeWorkRemotely", "age": "1h ago"},
    {"title": "QA Engineer / Test Developer", "company": "NERIS Analytics", "location": "Remote (Global)",
     "skills": ["Playwright", "Vue.js", "Laravel", "GitHub Actions", "WCAG 2.2"],
     "link": "https://weworkremotely.com/remote-jobs/neris-analytics-limited-qa-engineer-test-writing-developer", "source": "WeWorkRemotely", "age": "3h ago"},
    {"title": "QA Automation Engineer", "company": "Bookit.com", "location": "Remote (US)",
     "skills": ["Playwright", "TypeScript", "E2E Testing", "CI/CD", "HTML/DOM"],
     "link": "https://www.indeed.com/q-javascript-test-automation-playwright-jobs.html", "source": "Indeed", "age": "6h ago"},
    {"title": "QA Engineer III", "company": "RealPage", "location": "Remote",
     "skills": ["Playwright", "Selenium", "Full-stack Testing", "Senior Level"],
     "link": "https://weworkremotely.com/remote-jobs/realpage-qa-engineer-iii-selenium-playwright", "source": "WeWorkRemotely", "age": "9h ago"},
    {"title": "SDET with Playwright", "company": "AB2 Consulting", "location": "Okemos, MI (Hybrid)",
     "skills": ["Playwright", "SDET", "Automation Framework", "CI/CD"],
     "link": "https://www.indeed.com/q-playwright-test-automation-jobs.html", "source": "Indeed", "age": "11h ago"},
    {"title": "QA Automation Engineer", "company": "GG Tech Global", "location": "Remote",
     "skills": ["Playwright", "TypeScript", "Azure DevOps", "CI/CD", "5-7yrs exp"],
     "link": "https://www.indeed.com/q-playwright-test-automation-jobs.html", "source": "Indeed", "age": "15h ago"},
    {"title": "Sr. QA Engineer (Playwright)", "company": "Solvd, Inc.", "location": "Remote",
     "skills": ["Playwright", "Cypress", "Selenium", "Cucumber", "Jenkins", "Postman"],
     "link": "https://testdevjobs.com/tag/playwright-testing-jobs/", "source": "TestDevJobs", "age": "19h ago"},
    {"title": "Playwright QA / ETL & AI", "company": "DS Technologies", "location": "Remote (US)",
     "skills": ["Playwright", "ETL Testing", "AI/ML Testing", "SQL", "API Testing"],
     "link": "https://www.indeed.com/q-playwright-testing-l-remote-jobs.html", "source": "Indeed", "age": "23h ago"},
]

JOB_BOARDS = {
    "manual": [
        ("LinkedIn",       "https://www.linkedin.com/jobs/search/?keywords=manual+tester&f_TPR=r86400"),
        ("Indeed",         "https://www.indeed.com/jobs?q=manual+tester&fromage=1"),
        ("Naukri",         "https://www.naukri.com/manual-testing-jobs?jobAge=1"),
        ("Glassdoor",      "https://www.glassdoor.com/Job/manual-tester-jobs-SRCH_KO0,13.htm"),
        ("Wellfound",      "https://wellfound.com/jobs?role=qa-engineer"),
        ("WeWorkRemotely", "https://weworkremotely.com/remote-jobs/search?term=manual+tester"),
        ("RemoteOK",       "https://remoteok.com/remote-qa-jobs"),
        ("CutShort",       "https://cutshort.io/jobs/manual-testing-jobs"),
        ("Instahyre",      "https://www.instahyre.com/jobs/software-testing"),
        ("Hirist",         "https://www.hirist.tech/it-jobs/testing-qa-jobs"),
        ("Foundit",        "https://www.foundit.in/srp/results?query=manual+testing"),
        ("Dice",           "https://www.dice.com/jobs?q=manual+tester&datePosted=1"),
        ("TestDevJobs",    "https://testdevjobs.com/tag/manual-testing/"),
        ("NoFluffJobs",    "https://nofluffjobs.com/testing"),
        ("Monster",        "https://www.monster.com/jobs/search?q=manual+tester"),
        ("Himalayas",      "https://himalayas.app/jobs/qa-engineer"),
        ("BuiltIn",        "https://builtin.com/jobs/qa-testing"),
        ("Remote.co",      "https://remote.co/remote-jobs/qa-testing/"),
        ("Remotive",       "https://remotive.com/remote-jobs/qa"),
        ("QAJobsBoard",    "https://qajobsboard.com/"),
    ],
    "playwright": [
        ("LinkedIn",         "https://www.linkedin.com/jobs/search/?keywords=playwright+javascript+automation&f_TPR=r86400"),
        ("Indeed",           "https://www.indeed.com/jobs?q=playwright+javascript+automation&fromage=1"),
        ("Naukri",           "https://www.naukri.com/playwright-jobs?jobAge=1"),
        ("Glassdoor",        "https://www.glassdoor.com/Job/playwright-automation-jobs-SRCH_KO0,21.htm"),
        ("Wellfound",        "https://wellfound.com/jobs?role=qa-engineer&skills=playwright"),
        ("WeWorkRemotely",   "https://weworkremotely.com/remote-jobs/search?term=playwright+automation"),
        ("RemoteOK",         "https://remoteok.com/remote-playwright-jobs"),
        ("CutShort",         "https://cutshort.io/jobs/playwright-jobs"),
        ("Dice",             "https://www.dice.com/jobs?q=playwright+javascript+SDET&datePosted=1"),
        ("TestDevJobs",      "https://testdevjobs.com/tag/playwright-testing-jobs/"),
        ("Stack Overflow",   "https://stackoverflow.com/jobs?q=playwright+automation"),
        ("Himalayas",        "https://himalayas.app/jobs?q=playwright"),
        ("BuiltIn",          "https://builtin.com/jobs?q=playwright+automation"),
        ("Remotive",         "https://remotive.com/remote-jobs/software-dev?search=playwright"),
        ("RemoteRocketship", "https://www.remoterocketship.com/jobs/playwright"),
        ("Jobgether",        "https://jobgether.com/jobs?q=playwright+javascript"),
        ("NoFluffJobs",      "https://nofluffjobs.com/testing?criteria=requirement%3Dplaywright"),
        ("HiringCafe",       "https://hiring.cafe/?q=playwright+automation+engineer"),
        ("Upwork",           "https://www.upwork.com/nx/search/jobs/?q=playwright+javascript+automation"),
        ("Freelancer",       "https://www.freelancer.com/jobs/software-testing/playwright/"),
    ],
}

# ─── THEME ───────────────────────────────────────────────────────────────────

BG_DARK  = "#0a0a14"
BG_CARD  = "#111827"
ACCENT_B = "#6366f1"
ACCENT_G = "#10b981"
TEXT_PRI = "#f1f5f9"
TEXT_SEC = "#94a3b8"
TEXT_MUT = "#64748b"
PINK     = "#ec4899"
YELLOW   = "#f59e0b"

SOURCE_COLORS = {
    "Indeed":         "#2557A7",
    "WeWorkRemotely": "#1F8657",
    "CutShort":       "#5C35CC",
    "Dice":           "#E83E8C",
    "TestDevJobs":    "#34495E",
    "LinkedIn":       "#0A66C2",
}

FONT_TITLE  = ("Courier New", 22, "bold")
FONT_SUB    = ("Courier New", 13, "bold")
FONT_AUTHOR = ("Courier New", 13, "bold")   # same as subtitle
FONT_BOLD   = ("Courier New", 10, "bold")
FONT_NORMAL = ("Courier New", 10)
FONT_CARD   = ("Courier New", 13, "bold")
FONT_SMALL  = ("Courier New",  8)

PLACEHOLDER = "Filter by skill or title..."

# ─── MAIN APP ────────────────────────────────────────────────────────────────

class JobDashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Daily Job Alert — Manual Testing & Playwright JavaScript")
        self.geometry("1100x760")
        self.minsize(820, 600)
        self.configure(bg=BG_DARK)
        self.resizable(True, True)

        # ── State ──
        self.active_tab   = tk.StringVar(value="manual")
        self.active_view  = tk.StringVar(value="listings")
        self.filter_text  = tk.StringVar()
        self.saved_jobs   = set()
        self.last_refresh = datetime.now()

        # ── Build UI first, then attach trace ──
        self._build_ui()
        # Trace only fires render_listings; self.content is guaranteed to exist now
        self.filter_text.trace_add("write", self._on_filter_change)
        # Initial render
        self.render_listings()

    # ── TRACE ────────────────────────────────────────────────────────────────

    def _on_filter_change(self, *_):
        if self.active_view.get() == "listings":
            self.render_listings()

    # ── BUILD UI ─────────────────────────────────────────────────────────────

    def _build_ui(self):
        self._build_header()
        self._build_stats()
        self._build_tabs()
        # ctrl_row container — populated separately so it can be rebuilt
        self.ctrl_frame = tk.Frame(self, bg=BG_DARK)
        self.ctrl_frame.pack(fill="x", padx=24, pady=(0, 10))
        self._populate_ctrl_row()
        self._build_scroll_area()

    # ── HEADER ───────────────────────────────────────────────────────────────

    def _build_header(self):
        hdr = tk.Frame(self, bg=BG_DARK)
        hdr.pack(fill="x", padx=24, pady=(20, 0))

        # status dot
        tk.Label(hdr, text="⬤  LIVE FEED ACTIVE", bg=BG_DARK,
                 fg=ACCENT_G, font=("Courier New", 9, "bold")).pack(anchor="center")

        # main title
        tk.Label(hdr, text="Daily Job Alert", bg=BG_DARK,
                 fg=TEXT_PRI, font=FONT_TITLE).pack(anchor="center")

        # subtitle
        tk.Label(hdr,
                 text="Manual Testing  &  Playwright JavaScript",
                 bg=BG_DARK, fg=ACCENT_B,
                 font=FONT_SUB).pack(anchor="center")

        # author — centred, same font spec as subtitle
        tk.Label(hdr,
                 text="✦  PARTHA PATTANAYAK  ✦",
                 bg=BG_DARK, fg=YELLOW,
                 font=FONT_AUTHOR).pack(anchor="center", pady=(6, 2))

        # golden divider
        tk.Frame(hdr, bg=YELLOW, height=1).pack(fill="x", pady=(4, 6))

        # timestamp
        self.refresh_lbl = tk.Label(
            hdr, text=self._ts(), bg=BG_DARK,
            fg=TEXT_MUT, font=FONT_SMALL
        )
        self.refresh_lbl.pack(anchor="center", pady=(0, 6))

    def _ts(self):
        now = datetime.now()
        return (f"REFRESHED {self.last_refresh.strftime('%H:%M:%S')}  ·  "
                f"{now.strftime('%A %d %B %Y').upper()}")

    # ── STATS ────────────────────────────────────────────────────────────────

    def _build_stats(self):
        row = tk.Frame(self, bg=BG_DARK)
        row.pack(fill="x", padx=24, pady=12)

        specs = [
            ("Manual Jobs",     str(len(MANUAL_JOBS)),     ACCENT_B),
            ("Playwright Jobs", str(len(PLAYWRIGHT_JOBS)),  ACCENT_G),
            ("Job Boards",      "38+",                      YELLOW),
            ("Saved",           "0",                        PINK),
        ]
        self.stat_labels = {}
        for label, val, color in specs:
            f = tk.Frame(row, bg=BG_CARD)
            f.pack(side="left", padx=(0, 10), ipadx=16, ipady=8)
            v = tk.Label(f, text=val, bg=BG_CARD,
                         fg=color, font=("Courier New", 20, "bold"))
            v.pack()
            tk.Label(f, text=label.upper(), bg=BG_CARD,
                     fg=TEXT_MUT, font=FONT_SMALL).pack()
            self.stat_labels[label] = v

    # ── TABS ─────────────────────────────────────────────────────────────────

    def _build_tabs(self):
        row = tk.Frame(self, bg=BG_DARK)
        row.pack(fill="x", padx=24, pady=(0, 8))

        left = tk.Frame(row, bg=BG_DARK)
        left.pack(side="left")
        self._tab_btn(left, "🔵  Manual Testing",  "manual",    ACCENT_B)
        self._tab_btn(left, "🟣  Playwright / JS", "playwright", ACCENT_G)

        right = tk.Frame(row, bg=BG_DARK)
        right.pack(side="right")
        for v in ("listings", "boards", "saved"):
            self._view_btn(right, v.upper(), v)

    def _tab_btn(self, parent, text, value, color):
        def click():
            self.active_tab.set(value)
            self.filter_text.set("")
            self._refresh_view()
        tk.Button(parent, text=text, bg=BG_CARD, fg=color,
                  font=FONT_BOLD, relief="flat", padx=14, pady=6,
                  cursor="hand2",
                  activebackground=BG_DARK, activeforeground=color,
                  command=click).pack(side="left", padx=(0, 8))

    def _view_btn(self, parent, text, value):
        def click():
            self.active_view.set(value)
            self._repopulate_ctrl()
            self._refresh_view()
        tk.Button(parent, text=text, bg=BG_CARD,
                  fg=ACCENT_B if self.active_view.get() == value else TEXT_MUT,
                  font=("Courier New", 9, "bold"),
                  relief="flat", padx=10, pady=5, cursor="hand2",
                  activebackground=BG_CARD, activeforeground=ACCENT_B,
                  command=click).pack(side="left", padx=(0, 4))

    # ── CONTROL ROW ──────────────────────────────────────────────────────────

    def _repopulate_ctrl(self):
        for w in self.ctrl_frame.winfo_children():
            w.destroy()
        self._populate_ctrl_row()

    def _populate_ctrl_row(self):
        if self.active_view.get() == "listings":
            tk.Label(self.ctrl_frame, text="⌕", bg=BG_DARK,
                     fg=TEXT_MUT, font=("Courier New", 14)).pack(side="left")

            entry = tk.Entry(
                self.ctrl_frame, textvariable=self.filter_text,
                bg=BG_CARD, fg=TEXT_MUT,
                insertbackground=TEXT_PRI,
                font=("Courier New", 11),
                relief="flat", width=36
            )
            entry.pack(side="left", ipady=5, padx=(4, 12))
            entry.insert(0, PLACEHOLDER)

            def focus_in(e):
                if entry.get() == PLACEHOLDER:
                    entry.delete(0, "end")
                    entry.config(fg=TEXT_PRI)

            def focus_out(e):
                if entry.get().strip() == "":
                    self.filter_text.set("")
                    entry.insert(0, PLACEHOLDER)
                    entry.config(fg=TEXT_MUT)

            entry.bind("<FocusIn>",  focus_in)
            entry.bind("<FocusOut>", focus_out)

        tk.Button(self.ctrl_frame, text="↻  Refresh Now",
                  bg=BG_CARD, fg=ACCENT_G,
                  font=FONT_BOLD, relief="flat",
                  padx=14, pady=5, cursor="hand2",
                  activebackground=ACCENT_G, activeforeground=BG_DARK,
                  command=self._do_refresh).pack(side="left")

    # ── SCROLL AREA ──────────────────────────────────────────────────────────

    def _build_scroll_area(self):
        outer = tk.Frame(self, bg=BG_DARK)
        outer.pack(fill="both", expand=True, padx=24, pady=(0, 16))

        self.canvas = tk.Canvas(outer, bg=BG_DARK, highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)

        sb = ttk.Scrollbar(outer, orient="vertical", command=self.canvas.yview)
        sb.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=sb.set)

        # self.content is created HERE — before the trace is attached
        self.content = tk.Frame(self.canvas, bg=BG_DARK)
        self._cwin = self.canvas.create_window((0, 0), window=self.content, anchor="nw")

        self.content.bind("<Configure>", lambda e: self.canvas.configure(
            scrollregion=self.canvas.bbox("all")))
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfig(
            self._cwin, width=e.width))
        self.canvas.bind_all("<MouseWheel>",
            lambda e: self.canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

    # ── VIEWS ────────────────────────────────────────────────────────────────

    def _refresh_view(self):
        v = self.active_view.get()
        if   v == "listings": self.render_listings()
        elif v == "boards":   self.render_boards()
        elif v == "saved":    self.render_saved()

    def _clear(self):
        for w in self.content.winfo_children():
            w.destroy()
        self.canvas.yview_moveto(0)

    # listings ────────────────────────────────────────────────────────────────
    def render_listings(self):
        self._clear()
        jobs = MANUAL_JOBS if self.active_tab.get() == "manual" else PLAYWRIGHT_JOBS
        q = self.filter_text.get().strip().lower()
        if q and q != PLACEHOLDER.lower():
            jobs = [j for j in jobs
                    if q in j["title"].lower()
                    or any(q in s.lower() for s in j["skills"])]
        if not jobs:
            tk.Label(self.content, text="No jobs match your filter.",
                     bg=BG_DARK, fg=TEXT_MUT,
                     font=("Courier New", 12)).pack(pady=40)
            return
        for job in jobs:
            self._job_card(job)

    # boards ──────────────────────────────────────────────────────────────────
    def render_boards(self):
        self._clear()
        key    = self.active_tab.get()
        boards = JOB_BOARDS[key]
        color  = ACCENT_B if key == "manual" else ACCENT_G
        lbl    = "🔵 Manual Testing" if key == "manual" else "🟣 Playwright JS"

        tk.Label(self.content,
                 text=f"{lbl}  —  Click any board to open live 24 h search",
                 bg=BG_DARK, fg=TEXT_MUT,
                 font=FONT_SMALL).pack(anchor="w", pady=(4, 12))

        grid = tk.Frame(self.content, bg=BG_DARK)
        grid.pack(fill="both")
        for i, (name, url) in enumerate(boards):
            tk.Button(grid, text=f"⬡  {name}",
                      bg=BG_CARD, fg=color,
                      font=FONT_BOLD, relief="flat",
                      padx=10, pady=10, cursor="hand2", width=20,
                      activebackground=color, activeforeground=BG_DARK,
                      command=lambda u=url: webbrowser.open(u)
                      ).grid(row=i // 4, column=i % 4, padx=6, pady=6, sticky="ew")
        for c in range(4):
            grid.columnconfigure(c, weight=1)

    # saved ───────────────────────────────────────────────────────────────────
    def render_saved(self):
        self._clear()
        saved = [j for j in MANUAL_JOBS + PLAYWRIGHT_JOBS
                 if j["link"] in self.saved_jobs]
        if not saved:
            tk.Label(self.content,
                     text="♡  No saved jobs yet.\n\nGo to Listings and click  [ ♡ Save ]  on any card.",
                     bg=BG_DARK, fg=TEXT_MUT,
                     font=("Courier New", 12),
                     justify="center").pack(pady=60)
            return
        for job in saved:
            self._job_card(job, saved_view=True)

    # ── JOB CARD ─────────────────────────────────────────────────────────────

    def _job_card(self, job, saved_view=False):
        accent = PINK if saved_view else (
            ACCENT_B if self.active_tab.get() == "manual" else ACCENT_G)

        card = tk.Frame(self.content, bg=BG_CARD)
        card.pack(fill="x", pady=(0, 8))

        tk.Frame(card, bg=accent, width=4).pack(side="left", fill="y")

        inner = tk.Frame(card, bg=BG_CARD)
        inner.pack(side="left", fill="both", expand=True, padx=14, pady=12)

        # title + meta
        top = tk.Frame(inner, bg=BG_CARD)
        top.pack(fill="x")
        tk.Label(top, text=job["title"], bg=BG_CARD,
                 fg=TEXT_PRI, font=FONT_CARD, anchor="w").pack(side="left")
        tk.Label(top, text=job["age"], bg=BG_CARD,
                 fg=TEXT_MUT, font=FONT_SMALL).pack(side="right", padx=(0, 6))
        src_col = SOURCE_COLORS.get(job["source"], TEXT_MUT)
        tk.Label(top, text=f" {job['source']} ", bg=BG_CARD,
                 fg=src_col, font=("Courier New", 8, "bold")).pack(side="right")

        # company / location
        sub = tk.Frame(inner, bg=BG_CARD)
        sub.pack(fill="x", pady=(3, 0))
        tk.Label(sub, text=job["company"], bg=BG_CARD,
                 fg=TEXT_PRI, font=FONT_NORMAL).pack(side="left")
        tk.Label(sub, text="  ·  ", bg=BG_CARD,
                 fg=TEXT_MUT, font=FONT_NORMAL).pack(side="left")
        tk.Label(sub, text=f"  {job['location']}", bg=BG_CARD,
                 fg=TEXT_SEC, font=FONT_NORMAL).pack(side="left")

        # skill tags
        sr = tk.Frame(inner, bg=BG_CARD)
        sr.pack(fill="x", pady=(8, 0))
        for sk in job["skills"]:
            tag = tk.Label(sr, text=f" {sk} ", bg=BG_DARK,
                           fg="#a5b4fc", font=FONT_SMALL,
                           padx=2, pady=2, cursor="hand2")
            tag.pack(side="left", padx=(0, 4))
            tag.bind("<Button-1>",
                     lambda e, s=sk: (self.filter_text.set(s),
                                      self.active_view.set("listings"),
                                      self._repopulate_ctrl(),
                                      self.render_listings()))

        # action buttons
        bc = tk.Frame(card, bg=BG_CARD)
        bc.pack(side="right", padx=14, pady=12)

        tk.Button(bc, text="Apply →",
                  bg=BG_DARK, fg=accent,
                  font=FONT_BOLD, relief="flat",
                  padx=10, pady=5, cursor="hand2",
                  activebackground=accent, activeforeground=BG_DARK,
                  command=lambda u=job["link"]: webbrowser.open(u)
                  ).pack(fill="x")

        is_saved  = job["link"] in self.saved_jobs
        save_text = "♥ Saved" if is_saved else "♡ Save"
        save_fg   = PINK if is_saved else TEXT_MUT

        def toggle(link=job["link"]):
            if link in self.saved_jobs:
                self.saved_jobs.discard(link)
            else:
                self.saved_jobs.add(link)
            self.stat_labels["Saved"].config(text=str(len(self.saved_jobs)))
            self._refresh_view()

        tk.Button(bc, text=save_text,
                  bg=BG_DARK, fg=save_fg,
                  font=FONT_NORMAL, relief="flat",
                  padx=10, pady=4, cursor="hand2",
                  activebackground=PINK, activeforeground=BG_DARK,
                  command=toggle).pack(fill="x", pady=(5, 0))

    # ── REFRESH ──────────────────────────────────────────────────────────────

    def _do_refresh(self):
        self.last_refresh = datetime.now()
        self.refresh_lbl.config(text=self._ts())
        self._refresh_view()
        messagebox.showinfo(
            "Refreshed",
            f"✓  {len(MANUAL_JOBS)} Manual Testing jobs found\n"
            f"✓  {len(PLAYWRIGHT_JOBS)} Playwright JS jobs found\n\n"
            f"Last updated: {self.last_refresh.strftime('%H:%M:%S')}"
        )


# ─── ENTRY POINT ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app = JobDashboard()
    app.mainloop()
