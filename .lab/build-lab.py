import sys,re
S=sys.argv[1]
s=open('index.html').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a,s.count(a)); s=s.replace(a,b)
# wrapper off: the publish skeleton adds doctype, charset and viewport
i=s.index('<title>'); s=s[i:]
rep('<title>~john</title>','<title>Code for Monkeys Lab</title>')
rep('</head>\n<body>\n','')
rep('</body>\n</html>\n','')
# tunables
rep("  var PAD = 10; ","  var LAND_X = 0.47, LAND_Y = 0.53, STRIP_F = 0.173, FONT0 = 10;\n  var PAD = 10; ")
rep("AX = vw * ((narrow ? 0.5 : 0.47) + (narrow ? 0 : 0.03) * p)","AX = vw * ((narrow ? 0.5 : LAND_X) + (narrow ? 0 : 0.5 - LAND_X) * p)")
rep("AY = vh * (narrow ? 0.58 : 0.53) * (1 - p)","AY = vh * (narrow ? 0.58 : LAND_Y) * (1 - p)")
rep("    FS0 = vw < 560 ? 8 : 10;","    FS0 = Math.max(FSMIN + 0.5, vw < 560 ? FONT0 * 0.8 : FONT0);")
rep("    stripH = Math.round(Math.max(113, Math.min(167, vh * 0.173)));","    stripH = Math.round(Math.max(110, Math.min(vh * 0.6, vh * STRIP_F)));")
hook=open(S+'/lab-hook.js').read()
rep("  /* ── boot ── */",hook+"\n  /* ── boot ── */")
panel=open(S+'/lab-panel.html').read()
# defaults follow the site; a new storage key so old saved settings don't bring back the tall strip
panel=panel.replace("stripHeight: 0.26","stripHeight: 0.17").replace("var KEY = 'zob-design-lab';","var KEY = 'zob-design-lab-4';")
assert "stripHeight: 0.17" in panel and "zob-design-lab-4" in panel
s=s.rstrip('\n')+'\n'+panel+'\n'
open(S+'/lab.html','w').write(s)
