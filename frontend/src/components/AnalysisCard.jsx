export default function AnalysisCard({ text, setText, onSubmit, loading, textareaRef }) {
  return (
    <div className="w-full max-w-4xl mx-auto flex flex-col items-center rounded-3xl">
      <div className="glass-card rounded-3xl p-10 w-full fade-in-up">
        <h2 className="text-center text-3xl font-bold text-white">Analyze News Article</h2>
        <p className="text-center text-white/70 mt-3">Paste a news headline or article to check its authenticity.</p>

        <form onSubmit={onSubmit} className="flex flex-col items-center">
          <div className="w-full mt-8">
            <textarea
              ref={textareaRef}
              value={text}
              onChange={(e) => setText(e.target.value)}
              placeholder="Paste news article text here..."
              className="w-full bg-white/5 border border-white/10 rounded-xl p-5 text-white text-sm
                         placeholder:text-white/25 focus:outline-none focus:border-blue-500/40
                         focus:ring-1 focus:ring-blue-500/10 transition-all resize-none text-left"
              style={{ minHeight: '280px' }}
            />
            <div className="w-full flex justify-end mt-2">
              <span className="text-xs text-gray-500">{text.length} characters</span>
            </div>
          </div>

          <div className="flex justify-center mt-8 w-full">
            <button type="submit" disabled={loading || !text.trim()} className="btn-primary w-full max-w-md h-14 text-lg font-semibold rounded-xl">
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
          </div>
        </form>
      </div>
    </div>
  )
}
