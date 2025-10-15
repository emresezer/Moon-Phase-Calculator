<h1 align="center">🌕 Moon-Phase-Calculator</h1>
<p align="center">
  <em>Python-based lunar phase calculation and visualization project</em>
</p>

<hr>

<h2>🎯 Purpose & Scope</h2>
<p>
  <strong>Moon-Phase-Calculator</strong> is a Python project designed to calculate and visualize
  <strong>the current phase of the Moon</strong> based on a given date.
  It combines astronomical calculations with simple visualization, suitable for astronomers, photographers, and enthusiasts.
</p>
<ul>
  <li>Calculates the Moon's phase for today or any specified date.</li>
  <li>Displays textual representation of the Moon phase (e.g., New Moon, First Quarter, Full Moon).</li>
  <li>Computes approximate illumination percentage.</li>
  <li>Outputs results in a clear, readable format for easy observation planning.</li>
</ul>

<hr>

<h2>🧩 Project Structure</h2>

<pre>
📁 Moon-Phase-Calculator/
│
├── phase.py → English calculation and visualization script
├── evre.py → Turkish calculation and visualization script
└── README.md                → This file
</pre>

<hr>

<h2>⚙️ Installation & Usage</h2>
<ol>
  <li>Ensure <strong>Python 3.x</strong> is installed.</li>
  </li>
  <li>Run the script for today's Moon phase:
    <pre><code>python phase.py</code></pre>
  </li>
</ol>

<hr>

<h2>🧮 Physical / Astronomical Model</h2>

<h3>• Moon Phase Calculation:</h3>
<p>
  The phase of the Moon is computed based on its age in the synodic month (~29.53 days):
</p>

<pre>
Phase = (Current Date - Known New Moon Date) mod 29.53
</pre>

<p>
  Where:
  <ol>
    <li>New Moon</li>
    <li>Waxing Crescent</li>
    <li>First Quarter</li>
    <li>Waxing Gibbous</li>
    <li>Full Moon</li>
    <li>Waning Gibbous</li>
    <li>Last Quarter</li>
    <li>Waning Crescent</li>
  </ol>
</p>

<h3>• Illumination Calculation:</h3>
<pre>
Illumination (%) = (1 - cos(Phase × 2π / 29.53)) / 2 × 100
</pre>

<p>
  This approximation provides the visible illuminated fraction of the Moon's disk.
</p>

<hr>
