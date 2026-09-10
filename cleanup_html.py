from pathlib import Path

path = Path(r"c:\Users\Ieman Zahari\OneDrive\Documents\gimik\D10D_ENGINE_COMING_SOON2.HTML")
html = path.read_text(encoding='utf-8')

clean_css = '''
<style>
  :root {
    --neon-cyan: #00fff2;
    --neon-pink: #ff00d4;
    --neon-yellow: #ffe600;
    --bg-dark: #04060d;
  }

  * { box-sizing: border-box; }

  html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    background: var(--bg-dark);
    overflow: hidden;
    font-family: 'Courier New', monospace;
    color: var(--neon-cyan);
    -webkit-user-select: none;
    user-select: none;
    touch-action: none;
  }

  #stage {
    position: relative;
    width: 100%;
    height: 100vh;
    background-image:
      linear-gradient(rgba(0, 255, 242, 0.07) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0, 255, 242, 0.07) 1px, transparent 1px);
    background-size: 40px 40px;
    animation: gridMove 12s linear infinite;
  }

  @keyframes gridMove {
    from { background-position: 0 0, 0 0; }
    to { background-position: 0 40px, 40px 0; }
  }

  #stage::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at center, rgba(4, 6, 13, 0) 0%, rgba(4, 6, 13, 0.9) 75%);
    pointer-events: none;
  }

  #header {
    position: absolute;
    top: 16px;
    left: 0;
    right: 0;
    text-align: center;
    z-index: 5;
    pointer-events: none;
  }

  #header h1 {
    margin: 0;
    font-size: clamp(16px, 3vw, 30px);
    letter-spacing: 4px;
    color: var(--neon-cyan);
    text-shadow: 0 0 6px var(--neon-cyan), 0 0 18px var(--neon-cyan), 0 0 34px rgba(0, 255, 242, 0.6);
    animation: flicker 3.2s infinite;
  }

  #header p {
    margin: 6px 0 0;
    font-size: clamp(10px, 1.4vw, 14px);
    letter-spacing: 2px;
    color: var(--neon-pink);
    text-shadow: 0 0 8px var(--neon-pink);
    opacity: 0.9;
  }

  @keyframes flicker {
    0%, 19%, 21%, 23%, 80%, 100% { opacity: 1; }
    20%, 22% { opacity: 0.55; }
  }

  #dropzone {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 380px;
    height: 252px;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(2, 1fr);
    gap: 3px;
    border: 2px dashed rgba(0, 255, 242, 0.5);
    border-radius: 10px;
    box-shadow: 0 0 25px rgba(0, 255, 242, 0.25) inset, 0 0 25px rgba(0, 255, 242, 0.15);
    background: rgba(0, 255, 242, 0.03);
    z-index: 2;
    transition: opacity 0.5s ease;
  }

  .slot {
    position: relative;
    border: 1px dashed rgba(0, 255, 242, 0.25);
  }

  .slot::after {
    content: attr(data-label);
    position: absolute;
    top: 4px;
    left: 6px;
    font-size: 9px;
    letter-spacing: 2px;
    color: rgba(0, 255, 242, 0.35);
  }

  .slot.lit {
    border-color: var(--neon-yellow);
    box-shadow: 0 0 18px rgba(255, 230, 0, 0.5) inset;
    background: rgba(255, 230, 0, 0.05);
  }

  .piece {
    position: absolute;
    width: 200px;
    height: 133px;
    border-radius: 8px;
    box-shadow: 0 0 14px rgba(0, 255, 242, 0.55), 0 0 4px #000 inset;
    border: 2px solid rgba(0, 255, 242, 0.7);
    cursor: grab;
    z-index: 10;
    background-size: cover;
    transition: box-shadow 0.2s ease, border-color 0.2s ease;
    touch-action: none;
  }

  .piece:active { cursor: grabbing; }

  .piece.dragging {
    z-index: 50;
    box-shadow: 0 0 26px var(--neon-pink), 0 0 50px rgba(255, 0, 212, 0.5);
    border-color: var(--neon-pink);
  }

  .piece.placed {
    box-shadow: 0 0 20px var(--neon-yellow);
    border-color: var(--neon-yellow);
    cursor: default;
  }

  .piece .tag {
    position: absolute;
    bottom: 4px;
    right: 6px;
    font-size: 9px;
    letter-spacing: 2px;
    color: #fff;
    text-shadow: 0 0 4px #000;
    background: rgba(0, 0, 0, 0.35);
    padding: 1px 5px;
    border-radius: 3px;
  }

  #pc-tl { top: 24px; left: 24px; }
  #pc-tr { top: 24px; right: 24px; }
  #pc-bl { bottom: 24px; left: 24px; }
  #pc-br { bottom: 24px; right: 24px; }

  #progress {
    position: absolute;
    bottom: 14px;
    left: 0;
    right: 0;
    text-align: center;
    z-index: 5;
    font-size: 11px;
    letter-spacing: 3px;
    color: var(--neon-cyan);
    opacity: 0.7;
  }

  #hint {
    position: absolute;
    top: 56px;
    left: 0;
    right: 0;
    text-align: center;
    font-size: 10px;
    letter-spacing: 2px;
    color: rgba(0, 255, 242, 0.55);
    z-index: 5;
  }

  #finalImg {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) scale(0.001);
    width: 380px;
    height: 252px;
    object-fit: cover;
    border-radius: 10px;
    opacity: 0;
    filter: brightness(1);
    pointer-events: none;
    z-index: 80;
    transition: width 1s ease, height 1s ease, border-radius 0.8s ease, box-shadow 0.8s ease, opacity 0.6s ease, filter 0.8s ease;
  }

  #overlay {
    position: fixed;
    inset: 0;
    z-index: 100;
    display: none;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    background: radial-gradient(ellipse at center, rgba(2, 3, 8, 0.15) 0%, rgba(2, 3, 8, 0.55) 65%, rgba(2, 3, 8, 0.82) 100%);
    text-align: center;
    opacity: 0;
  }

  #overlay.show {
    display: flex;
    animation: overlayFade 0.6s ease forwards;
  }

  @keyframes overlayFade {
    from { opacity: 0; }
    to { opacity: 1; }
  }

  #overlay .scan {
    position: absolute;
    inset: 0;
    pointer-events: none;
    background: repeating-linear-gradient(0deg, rgba(0, 255, 242, 0.05) 0px, rgba(0, 255, 242, 0.05) 1px, transparent 2px, transparent 4px);
    mix-blend-mode: screen;
  }

  #bigtext {
    position: relative;
    font-size: clamp(30px, 7.5vw, 76px);
    font-weight: 900;
    letter-spacing: 2px;
    font-family: 'Arial Black', 'Courier New', sans-serif;
    color: #fff;
    text-transform: uppercase;
    -webkit-text-stroke: 2px rgba(0, 255, 242, 0.9);
    text-stroke: 2px rgba(0, 255, 242, 0.9);
    text-shadow: 0 0 8px var(--neon-cyan), 0 0 20px var(--neon-cyan), 0 0 40px var(--neon-pink), 0 0 70px var(--neon-pink), 0 0 110px var(--neon-pink);
    opacity: 0;
    transform: scale(0.7);
    line-height: 1.25;
  }

  #bigtext.in {
    animation: popIn 0.7s cubic-bezier(0.2, 1.4, 0.4, 1) forwards, glitch 2.4s 0.8s infinite;
  }

  @keyframes popIn {
    0% { opacity: 0; transform: scale(0.4) rotateX(40deg); }
    60% { opacity: 1; transform: scale(1.08) rotateX(0deg); }
    100% { opacity: 1; transform: scale(1) rotateX(0deg); }
  }

  @keyframes glitch {
    0%, 93%, 100% { transform: translate(0, 0); text-shadow: 0 0 8px var(--neon-cyan), 0 0 20px var(--neon-cyan), 0 0 40px var(--neon-pink), 0 0 70px var(--neon-pink); }
    94% { transform: translate(-3px, 1px); }
    95% { transform: translate(3px, -1px); color: var(--neon-yellow); }
    96% { transform: translate(-2px, -1px); }
    97% { transform: translate(0, 0); }
  }

  #subtext {
    margin-top: 18px;
    font-size: clamp(11px, 1.6vw, 16px);
    letter-spacing: 6px;
    color: var(--neon-yellow);
    text-shadow: 0 0 10px var(--neon-yellow);
    opacity: 0;
  }

  #subtext.in { animation: fadeUp 1s 0.5s forwards; }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(14px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .neon-btn {
    position: absolute;
    z-index: 60;
    font-family: 'Courier New', monospace;
    font-weight: bold;
    letter-spacing: 2px;
    font-size: 12px;
    color: var(--neon-cyan);
    background: rgba(0, 255, 242, 0.06);
    border: 1px solid rgba(0, 255, 242, 0.7);
    border-radius: 6px;
    padding: 8px 16px;
    cursor: pointer;
    text-shadow: 0 0 6px var(--neon-cyan);
    box-shadow: 0 0 12px rgba(0, 255, 242, 0.35);
    transition: all 0.2s ease;
  }

  .neon-btn:hover {
    background: rgba(0, 255, 242, 0.18);
    box-shadow: 0 0 20px rgba(0, 255, 242, 0.7);
  }

  .neon-btn:active { transform: scale(0.96); }

  #restartBtn {
    bottom: 52px;
    left: 50%;
    transform: translateX(-50%);
  }

  #restartBtnOverlay {
    position: absolute;
    bottom: 34px;
    left: 50%;
    margin-top: 0;
    color: var(--neon-yellow);
    border-color: var(--neon-yellow);
    text-shadow: 0 0 6px var(--neon-yellow);
    box-shadow: 0 0 12px rgba(255, 230, 0, 0.35);
    opacity: 0;
  }

  #restartBtnOverlay.in { animation: fadeUpCenter 1s 1s forwards; }

  @keyframes fadeUpCenter {
    from { opacity: 0; transform: translate(-50%, 14px); }
    to { opacity: 1; transform: translate(-50%, 0); }
  }

  #restartBtnOverlay:hover {
    background: rgba(255, 230, 0, 0.15);
    box-shadow: 0 0 20px rgba(255, 230, 0, 0.7);
  }

  #finalDriveImg {
    max-width: 900px;
    width: 80%;
    margin-top: 80px;
    filter: drop-shadow(0 0 80px #00fff2);
  }
</style>
'''

clean_script = '''
<script>
  (() => {
    const stage = document.getElementById('stage');
    const dropzone = document.getElementById('dropzone');
    const pieces = Array.from(document.querySelectorAll('.piece'));
    const finalImg = document.getElementById('finalImg');
    const countEl = document.getElementById('count');
    const overlay = document.getElementById('overlay');
    const bigText = document.getElementById('bigtext');
    const subText = document.getElementById('subtext');
    const restartBtnOverlay = document.getElementById('restartBtnOverlay');

    const homePositions = {};
    const PIECE_W = 200;
    const PIECE_H = 133;

    let audioCtx = null;
    let musicStarted = false;
    let musicGain = null;
    let themeGain = null;
    let bgDuckTimeout = null;
    let lockedCount = 0;
    let lastLaser = 0;

    function getCtx() {
      if (!audioCtx) {
        const AudioCtor = window.AudioContext || window.webkitAudioContext;
        audioCtx = new AudioCtor();
      }
      if (audioCtx.state === 'suspended') {
        audioCtx.resume();
      }
      return audioCtx;
    }

    function playTone({ type, end, duration, gainValue, wave }) {
      try {
        const ctx = getCtx();
        const start = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = wave;
        osc.frequency.setValueAtTime(type, start);
        osc.frequency.exponentialRampToValueAtTime(end, start + duration);
        gain.gain.setValueAtTime(0.0001, start);
        gain.gain.exponentialRampToValueAtTime(gainValue, start + 0.02);
        gain.gain.exponentialRampToValueAtTime(0.0001, start + duration);
        osc.connect(gain).connect(ctx.destination);
        osc.start(start);
        osc.stop(start + duration);
      } catch (error) {
        // Audio is optional.
      }
    }

    function playLaser() {
      playTone({ type: 1600, end: 180, duration: 0.15, gainValue: 0.18, wave: 'sawtooth' });
    }

    function playLock() {
      playTone({ type: 420, end: 880, duration: 0.18, gainValue: 0.2, wave: 'square' });
    }

    function playPowerUp() {
      playTone({ type: 120, end: 1200, duration: 1.0, gainValue: 0.22, wave: 'sine' });
    }

    function startBackgroundMusic() {
      if (musicStarted) return;
      musicStarted = true;

      const ctx = getCtx();
      musicGain = ctx.createGain();
      musicGain.gain.value = 0.045;
      musicGain.connect(ctx.destination);

      const notes = [174.61, 207.65, 233.08, 261.63, 233.08, 207.65];
      const noteDuration = 1.1;
      let step = 0;

      function scheduleBar() {
        const startAt = ctx.currentTime + 0.05;
        for (let i = 0; i < notes.length; i += 1) {
          const freq = notes[(step + i) % notes.length];
          const start = startAt + i * noteDuration;

          const osc = ctx.createOscillator();
          osc.type = 'triangle';
          osc.frequency.value = freq;
          const gain = ctx.createGain();
          gain.gain.setValueAtTime(0.0001, start);
          gain.gain.exponentialRampToValueAtTime(1, start + 0.08);
          gain.gain.exponentialRampToValueAtTime(0.0001, start + noteDuration * 0.92);
          osc.connect(gain).connect(musicGain);
          osc.start(start);
          osc.stop(start + noteDuration);

          const bass = ctx.createOscillator();
          bass.type = 'sine';
          bass.frequency.value = freq / 2;
          const bassGain = ctx.createGain();
          bassGain.gain.setValueAtTime(0.0001, start);
          bassGain.gain.exponentialRampToValueAtTime(0.5, start + 0.1);
          bassGain.gain.exponentialRampToValueAtTime(0.0001, start + noteDuration * 0.9);
          bass.connect(bassGain).connect(musicGain);
          bass.start(start);
          bass.stop(start + noteDuration);
        }
        step += notes.length;
      }

      scheduleBar();
      setInterval(scheduleBar, notes.length * noteDuration * 1000 - 60);
    }

    function resetAll() {
      overlay.classList.remove('show');
      bigText.classList.remove('in');
      subText.classList.remove('in');
      restartBtnOverlay.classList.remove('in');

      lockedCount = 0;
      countEl.textContent = lockedCount;

      finalImg.style.transition = 'none';
      finalImg.style.opacity = '0';
      finalImg.style.transform = 'translate(-50%, -50%) scale(0.001)';
      finalImg.style.boxShadow = '0 0 0px rgba(0,255,242,0)';
      finalImg.style.width = '380px';
      finalImg.style.height = '252px';
      finalImg.style.borderRadius = '10px';
      finalImg.style.filter = 'brightness(1)';

      if (themeGain) {
        try {
          const ctx = getCtx();
          themeGain.gain.cancelScheduledValues(ctx.currentTime);
          themeGain.gain.setValueAtTime(themeGain.gain.value, ctx.currentTime);
          themeGain.gain.linearRampToValueAtTime(0.0001, ctx.currentTime + 0.2);
        } catch (error) {
          // Ignore audio reset errors.
        }
      }

      if (bgDuckTimeout) {
        clearTimeout(bgDuckTimeout);
        bgDuckTimeout = null;
      }

      if (musicGain) {
        try {
          const ctx = getCtx();
          musicGain.gain.cancelScheduledValues(ctx.currentTime);
          musicGain.gain.setValueAtTime(musicGain.gain.value, ctx.currentTime);
          musicGain.gain.linearRampToValueAtTime(0.045, ctx.currentTime + 0.4);
        } catch (error) {
          // Ignore audio reset errors.
        }
      }

      dropzone.style.transition = 'none';
      dropzone.style.opacity = '1';
      Array.from(dropzone.querySelectorAll('.slot')).forEach(slot => slot.classList.remove('lit'));

      pieces.forEach(piece => {
        piece.classList.remove('placed', 'dragging');
        piece.style.transition = 'none';
        piece.style.opacity = '1';
        piece.style.width = PIECE_W + 'px';
        piece.style.height = PIECE_H + 'px';
        const home = homePositions[piece.id];
        piece.style.left = home.left + 'px';
        piece.style.top = home.top + 'px';
      });

      void stage.offsetWidth;
      pieces.forEach(piece => piece.style.transition = '');
      dropzone.style.transition = '';
      finalImg.style.transition = '';
    }

    function triggerMerge() {
      playPowerUp();
      dropzone.style.transition = 'opacity 0.5s';
      dropzone.style.opacity = '0';

      finalImg.style.transition = 'none';
      finalImg.style.transform = 'translate(-50%, -50%) scale(1)';
      finalImg.style.filter = 'brightness(1)';
      void finalImg.offsetWidth;
      finalImg.style.transition = 'opacity 0.6s ease';
      finalImg.style.opacity = '1';

      setTimeout(() => {
        finalImg.style.transition = 'width 1.1s ease, height 1.1s ease, border-radius 1s ease, box-shadow 1s ease';
        finalImg.style.width = '100%';
        finalImg.style.height = '100%';
        finalImg.style.borderRadius = '0px';
        finalImg.style.boxShadow = '0 0 60px rgba(0,255,242,0.5) inset';
      }, 700);

      setTimeout(() => {
        finalImg.style.transition = 'filter 0.8s ease';
        finalImg.style.filter = 'brightness(0.5)';
      }, 2000);

      setTimeout(() => {
        overlay.classList.add('show');
        bigText.classList.add('in');
        subText.classList.add('in');
        restartBtnOverlay.classList.add('in');
      }, 2500);
    }

    function slotRect(slot) {
      return slot.getBoundingClientRect();
    }

    function pieceOverSlot(pieceRect, slotRectEl, margin) {
      const cx = pieceRect.left + pieceRect.width / 2;
      const cy = pieceRect.top + pieceRect.height / 2;
      return cx >= slotRectEl.left - margin && cx <= slotRectEl.right + margin &&
        cy >= slotRectEl.top - margin && cy <= slotRectEl.bottom + margin;
    }

    pieces.forEach(piece => {
      let dragging = false;
      let offsetX = 0;
      let offsetY = 0;

      piece.addEventListener('pointerdown', event => {
        if (piece.classList.contains('placed')) return;

        dragging = true;
        piece.classList.add('dragging');
        piece.setPointerCapture(event.pointerId);

        const rect = piece.getBoundingClientRect();
        offsetX = event.clientX - rect.left;
        offsetY = event.clientY - rect.top;
        piece.style.left = rect.left + 'px';
        piece.style.top = rect.top + 'px';
        piece.style.right = 'auto';
        piece.style.bottom = 'auto';

        getCtx();
        startBackgroundMusic();
      });

      piece.addEventListener('pointermove', event => {
        if (!dragging) return;

        const stageRect = stage.getBoundingClientRect();
        const x = event.clientX - offsetX - stageRect.left;
        const y = event.clientY - offsetY - stageRect.top;
        piece.style.left = x + 'px';
        piece.style.top = y + 'px';

        const targetSlot = document.getElementById(piece.dataset.target);
        const slotRectEl = slotRect(targetSlot);
        const pr = piece.getBoundingClientRect();
        targetSlot.classList.toggle('lit', pieceOverSlot(pr, slotRectEl, 24));

        const now = performance.now();
        if (now - lastLaser > 130) {
          playLaser();
          lastLaser = now;
        }
      });

      const endDrag = () => {
        if (!dragging) return;

        dragging = false;
        piece.classList.remove('dragging');

        const targetSlot = document.getElementById(piece.dataset.target);
        targetSlot.classList.remove('lit');

        const slotRectEl = slotRect(targetSlot);
        const pr = piece.getBoundingClientRect();
        const isOver = pieceOverSlot(pr, slotRectEl, 24);

        if (isOver) {
          const stageRect = stage.getBoundingClientRect();
          piece.style.left = (slotRectEl.left - stageRect.left) + 'px';
          piece.style.top = (slotRectEl.top - stageRect.top) + 'px';
          piece.style.width = slotRectEl.width + 'px';
          piece.style.height = slotRectEl.height + 'px';
          piece.classList.add('placed');
          playLock();
          lockedCount += 1;
          countEl.textContent = lockedCount;

          if (lockedCount === pieces.length) {
            setTimeout(triggerMerge, 350);
          }
        } else {
          piece.style.transition = 'left .35s ease, top .35s ease';
          const homeRect = homePositions[piece.id];
          piece.style.left = homeRect.left + 'px';
          piece.style.top = homeRect.top + 'px';
          setTimeout(() => { piece.style.transition = ''; }, 380);
        }
      };

      piece.addEventListener('pointerup', endDrag);
      piece.addEventListener('pointercancel', endDrag);
    });

    window.addEventListener('load', () => {
      pieces.forEach(piece => {
        const stageRect = stage.getBoundingClientRect();
        const rect = piece.getBoundingClientRect();
        homePositions[piece.id] = {
          left: rect.left - stageRect.left,
          top: rect.top - stageRect.top,
        };
      });
    });

    document.getElementById('restartBtn').addEventListener('click', () => {
      startBackgroundMusic();
      resetAll();
    });

    restartBtnOverlay.addEventListener('click', () => {
      startBackgroundMusic();
      resetAll();
    });
  })();
</script>
'''

first_style = html.find('<style>')
first_style_end = html.find('</style>', first_style)
if first_style == -1 or first_style_end == -1:
    raise ValueError('Could not find first style block')
html = html[:first_style] + clean_css + html[first_style_end + len('</style>'):]

first_script = html.find('<script>')
first_script_end = html.find('</script>', first_script)
if first_script == -1 or first_script_end == -1:
    raise ValueError('Could not find first script block')
html = html[:first_script] + clean_script + html[first_script_end + len('</script>'):]

path.write_text(html, encoding='utf-8')
print('Cleaned HTML saved to', path)
print('style count:', html.count('<style>'))
print('script count:', html.count('<script>'))
