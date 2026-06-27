export default function AnalysisCard({ text, setText, onSubmit, loading, textareaRef }) {
  return (
    <div className="analyzer-card glass-card fade-in-up glow">
      <h2 className="text-lg font-semibold text-white">Analyze News Article</h2>
      <p className="text-white/40 text-sm analyzer-subtitle">Paste a news headline or article to check its authenticity.</p>

      <form onSubmit={onSubmit}>
        <textarea
          ref={textareaRef}
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Paste news article text here..."
          rows={9}
          className="w-full bg-white/5 border border-white/10 rounded-xl p-5 text-white text-sm
                     placeholder:text-white/25 focus:outline-none focus:border-blue-500/50
                     focus:ring-1 focus:ring-blue-500/20 transition-all resize-none
                     custom-scrollbar"
        />
        <div className="flex justify-end character-counter">
          <span className="text-xs text-white/30">{text.length} characters</span>
        </div>

        <button
          type="submit"
          disabled={loading || !text.trim()}
          className="btn-primary w-full analyze-btn"
        >
          {loading ? (
            <span className="flex items-center justify-center gap-3">
              <span className="spinner !w-5 !h-5 !border-2" />
              Analyzing...
            </span>
          ) : (
            <span className="flex items-center justify-center gap-2">
              <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                <path strokeLinecap="round" strokeLinejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
              Analyze Article
            </span>
          )}
        </button>
      </form>
    </div>
  )
}
