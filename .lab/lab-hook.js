  /* ── the design lab's handle on the scene ── */
  function hexRGB(h) { var n = parseInt(h.slice(1), 16); return [(n >> 16) & 255, (n >> 8) & 255, n & 255]; }
  function packC(c, k) { return (255 << 24) | (Math.round(c[2] * k) << 16) | (Math.round(c[1] * k) << 8) | Math.round(c[0] * k); }
  window.__lab = {
    set: function (o) {
      if ('heroH' in o) HERO_H = o.heroH;
      if ('landX' in o) LAND_X = o.landX;
      if ('landY' in o) LAND_Y = o.landY;
      if ('font' in o) FONT0 = o.font;
      if ('strip' in o) STRIP_F = o.strip;
      if ('matW' in o) MW = o.matW;
      if ('matD' in o) MD = o.matD;
      if ('pitch' in o) PITCH = o.pitch;
      if ('yaw' in o) CAMYAW = o.yaw;
      if ('matColor' in o) {
        var c = hexRGB(o.matColor);
        MAT_TOP = packC(c, 1); MAT_SEAM = packC(c, 0.74); MAT_EDGE = packC(c, 0.6); MAT_SIDE = packC(c, 0.48);
      }
      if ('banker' in o) MAT[4] = hexRGB(o.banker).concat(0);
      if ('player' in o) MAT[0] = hexRGB(o.player).concat(0);
      if ('pal' in o && o.pal !== pal) { pal = o.pal; mixColors(); }
      if ('speed' in o && o.speed !== G.speed) { G.speed = o.speed; G.acc = 0; }
      resize(); draw();
    }
  };
