export default function NewsForm({ text, setText, onSubmit, loading }) {
  const charCount = text.length

  return (
    <form onSubmit={onSubmit} className="space-y-4">
      <div>
        <label htmlFor="news-text" className="block text-sm font-medium text-gray-700 mb-1">
          Paste or type a news article below
        </label>
        <textarea
          id="news-text"
          rows={8}
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Paste a news article headline or full text here…"
          className="w-full border border-gray-300 rounded-lg p-4 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 resize-y"
        />
        <div className="flex justify-between items-center mt-1">
          <span className="text-xs text-gray-400">{charCount} characters</span>
        </div>
      </div>

      <button
        type="submit"
        disabled={loading || !text.trim()}
        className="w-full bg-blue-600 hover:bg-blue-700 disabled:bg-blue-300 text-white font-medium py-3 px-6 rounded-lg transition-colors cursor-pointer disabled:cursor-not-allowed"
      >
        {loading ? 'Analyzing…' : 'Analyze Article'}
      </button>
    </form>
  )
}
