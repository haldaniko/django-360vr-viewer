document.addEventListener('DOMContentLoaded', () => {
  const video = document.getElementById('video360');
  const playButton = document.getElementById('playButton');
  const videosphere = document.getElementById('videosphere');

  const url = window.dashManifestUrl;

  const player = dashjs.MediaPlayer().create();

  player.updateSettings({
    streaming: {
      buffer: {
        stableBufferTime: 3,
        bufferTimeAtTopQuality: 5,
        bufferTimeAtTopQualityLongForm: 8,
        fastSwitchEnabled: true
      }
    }
  });

  player.initialize(video, url, false);

  player.on(dashjs.MediaPlayer.events.ERROR, (e) => {
    console.error('Dash.js error:', e);
    if (e.error && e.error.code === 'QuotaExceededError') {
      player.reset();
      player.initialize(video, url, false);
      video.pause();
      if (videosphere) videosphere.setAttribute('visible', 'false');
    }
  });

  video.addEventListener('loadeddata', () => {
    if (videosphere) videosphere.setAttribute('visible', 'true');
  });

  playButton.addEventListener('click', () => {
    player.play();
    video.muted = false;
    video.play().catch(e => console.error('Video play failed:', e));
    playButton.style.display = 'none';
  });
});
