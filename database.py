import numpy as np
import sys,os
import json

papers = {}
submitted = True
published = False
proceedings = False
others = True

talks  = {}
conferences= True
seminars = True
lectures = False
posters = True
outreach = False

group  = {}
fellowships = False
postdocs = False
phd = False
msc = False
bsc = True


if submitted:

    papers['submitted'] = {}
    papers['submitted']['label'] = 'Submitted papers'
    papers['submitted']['data'] = []

    papers['submitted']['data'].append({
        "title":    "Black-hole ringdown with templates capturing spin precession: a critical re-analysis of GW190521",
        "author":   "C. Anselmo, C. Pacilio, D. Gerosa",
        "journal":  "",
        "link":     "",
        "arxiv":    "arXiv:2512.05193 [gr-qc]",
        "ads":      "2025arXiv251205193A,
        "inspire":  "Anselmo:2025ehx",
        "more":     ""
        })

if published:
    papers['published'] = {}
    papers['published']['label'] = 'Papers published in major peer-reviewed journals'
    papers['published']['data'] = []


if proceedings:
    papers['proceedings'] = {}
    papers['proceedings']['label'] = 'Other publications (white papers, proceedings, etc.)'
    papers['proceedings']['data'] = []


if others:
    papers['others'] = {}
    papers['others']['label'] = ''
    papers['others']['data'] = []


if conferences:
    talks['conferences'] = {}
    talks['conferences']['label'] = 'Talks at conferences'
    talks['conferences']['data'] = []

    talks['conferences']['data'].append({
        "title":    "Quasi normal mode detectability by future space detectors",
        "what":     "Lunar Gravitational-Wave Antenna Workshop",
        "where":    "Rome, Italy",
        "when":     "Oct 2024",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Ringdown analysis with simulation-based inference",
        "what":     "Theoretical Horizons in Unraveling Relativity, Astrophysics, and Mergers (THURAM)",
        "where":    "L'Aquila, Italy",
        "when":     "May 2025",
        "invited":  False,
        "more":     ""
        })
    
    talks['conferences']['data'].append({
        "title":    "Improved gravitational wave parameter estimation with SBI and secondary mode marginalization",
        "what":     "AIslands 2025: Bute",
        "where":    "Rothesay, Isle of Bute, Scotland",
        "when":     "May 2025",
        "invited":  False,
        "more":     ""
        })
        
    talks['conferences']['data'].append({
        "title":    "Improved gravitational wave parameter estimation with SBI and secondary mode marginalization",
        "what":     "AIslands 2025: Bute",
        "where":    "Rothesay, Isle of Bute, Scotland",
        "when":     "May 2025",
        "invited":  False,
        "more":     ""
        })


if seminars:
    talks['seminars'] = {}
    talks['seminars']['label'] = 'Talks at department seminars'
    talks['seminars']['data'] = []


if lectures:
    talks['lectures'] = {}
    talks['lectures']['label'] = 'Lectures at PhD schools'
    talks['lectures']['data'] = []


if posters:
    talks['posters'] = {}
    talks['posters']['label'] = 'Posters at conferences'
    talks['posters']['data'] = []

    talks['posters']['data'].append({
        "title":    "Exploitation of gravitational-wave data",
        "what":    "Milano-Bicocca Physics Department 25th anniversary",
        "where":    "Milan, Italy",
        "when":     "Sep 2024",
        "invited":  True,
        "more":     ""
        })


if outreach:
    talks['outreach'] = {}
    talks['outreach']['label'] = 'Outreach talks'
    talks['outreach']['data'] = []


if fellowships:

    group['fellowships'] = {}
    group['fellowships']['labelshort'] = 'Postdoc fellowships'
    group['fellowships']['labellong'] = 'Postdoc external fellowship sponsor'
    group['fellowships']['data'] = []

    
if postdocs:
    group['postdocs'] = {}
    group['postdocs']['labelshort'] = 'Postdocs (hired)'
    group['postdocs']['labellong'] = 'Hired postdocs'
    group['postdocs']['data'] = []
    
 
if phd:
    group['phd'] = {}
    group['phd']['labelshort'] = 'PhD students'
    group['phd']['labellong'] = 'PhD student supervisor'
    group['phd']['data'] = []


if msc:
    group['msc'] = {}
    group['msc']['labelshort'] = 'MSc students'
    group['msc']['labellong'] = 'MSc student mentoring'
    group['msc']['data'] = []


if bsc:
    group['bsc'] = {}
    group['bsc']['labelshort'] = 'BSc students'
    group['bsc']['labellong'] = 'BSc student projects'
    group['bsc']['data'] = []

    group['bsc']['data'].append({
        "name":     "Alessandro Zappietro",
        "where":    "Milano-Bicocca and Pavia",
        "what":     "BSc thesis",
        "year":     "2026",
        "current":  True
        })
