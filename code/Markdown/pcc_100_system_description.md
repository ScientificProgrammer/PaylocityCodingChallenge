# 1 Paylocity Coding Challenge - System Configuration Details

<div style="font-size: 1.5em; padding-bottom: 0;">

Eric Milgram, PhD

</div>

<table>
<tbody>
<tr>
<td style="padding: 0; display: none;">
<a href="https://github.com/ScientificProgrammer/PaylocityCodingChallenge">ScientificProgrammer/PaylocityCodingChallenge</a>
</td>
</tr>
<tr>
<td style="padding: 0;">
Created: December 23, 2021
</td>
</tr>
<tr>
<td style="padding: 0;">
Last Updated: 2022-01-19 05:13:39</span>
</td>
</tr>
</tbody>
</table>

## 1.1 Overview

This page contains a summary of the key software components, frameworks,
and operating systems that were used to complete the Paylocity Coding
Challenge.

## 1.2 OS PARAMS

<table class="table table-striped table-condensed table-bordered" style="margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:left;"> PARAMETER </th>
   <th style="text-align:left;"> VALUE </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> OS Name </td>
   <td style="text-align:left;"> Microsoft Windows 11 Home </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Version </td>
   <td style="text-align:left;"> 10.0.22000 Build 22000 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> System Type </td>
   <td style="text-align:left;"> x64-based PC </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Processor </td>
   <td style="text-align:left;"> Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz, 2801 Mhz, 4 Core(s), 8 Logical Processor(s) </td>
  </tr>
  <tr>
   <td style="text-align:left;"> BIOS Version/Date </td>
   <td style="text-align:left;"> LENOVO 4KCN45WW, 1/11/2019 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Locale </td>
   <td style="text-align:left;"> United States </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Installed Physical Memory (RAM) </td>
   <td style="text-align:left;"> 16.0 GB </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Total Physical Memory </td>
   <td style="text-align:left;"> 15.9 GB </td>
  </tr>
</tbody>
</table>

## 1.3 Editors/IDEs

1.  `vim` on *Debian* running under Windows Subsystem for Linux (WSL)  
       

    <pre>
    eric@Y520-ERIC:~$ cat /etc/os-release
    PRETTY_NAME="Debian GNU/Linux 10 (buster)"
    NAME="Debian GNU/Linux"
    VERSION_ID="10"
    VERSION="10 (buster)"
    VERSION_CODENAME=buster
    ID=debian
    HOME_URL="https://www.debian.org/"
    SUPPORT_URL="https://www.debian.org/support"
    BUG_REPORT_URL="https://bugs.debian.org/"
    </pre>

     

2.  `Sublime Text 4` on `Windows - Build 4126` with the following
    installed plug-ins

    1.  `LSP` & `LSP-pylsp` configured for `flake8 4.0.1`
        (`CPython 3.10.1` on `Windows`)

    2.  Lint Checks

        1.  `pycodestyle 2.8.0`

        2.  `pyflakes 2.4.0`

        3.  `mccabe: 0.6.1` (*McCabe complexity checking*)

    3.  Auto-formatting provided by `Python Black`

## 1.4 Database Administration Tool - pgAdmin 4 (Microsoft Windows x64)

![**FIGURE**: pgAdmin 4 GUI for MS
Windows](D:/GoogleDrive/eric.milgram/Career/Job%20Prospects/2021-11-09%20Paylocity/020%20Paylocity%20Coding%20Challenge/Paylocity%20Coding%20Challenge/img/fig_pgAdmin4_gui_for_Win11_x64.png)

### 1.4.1 pgAdmin4 Specifications

The following table contains a summary of the pgAdmin4 specification
values for the instance that I used to complete this coding challenge.

| Parameter        | Value                                                 |
|:-----------------|:------------------------------------------------------|
| Version          | 6.3                                                   |
| Application Mode | Desktop                                               |
| Current User     | <pgadmin4@pgadmin.org>                                |
| NW.js Version    | 0.59.0                                                |
| Browser          | Chromium 96.0.4664.55                                 |
| Operating System | Windows-10-10.0.22000-SP0                             |
| Release Date     | Dec 16, 2021                                          |
| Download Link    | <https://www.pgadmin.org/download/pgadmin-4-windows/> |

       
