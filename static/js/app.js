function studioApp() {
  return {
    tab: 'text',
    prompt: '',
    text: '',
    image: '',
    video: '',
    loading: false,

    async handleGenerate() {
      if (!this.prompt) return alert("Please enter a prompt!");
      this.loading = true;
      this.text = this.image = this.video = '';

      if (this.tab === 'text') {
        const res = await fetch('/text/generate', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ prompt: this.prompt })
        });
        const data = await res.json();
        this.text = data.response;
      }

      else if (this.tab === 'image') {
        const res = await fetch('/image/generate', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ prompt: this.prompt })
        });
        const blob = await res.blob();
        this.image = URL.createObjectURL(blob);
      }

      else if (this.tab === 'video') {
        // Placeholder — video API integration can be added here
        this.video = "https://samplelib.com/lib/preview/mp4/sample-5s.mp4";
      }

      this.loading = false;
    }
  };
}
