export default function PredictionCard({ result }) {
  const isFake = result.prediction === 'Fake News'
  const confidence = (result.confidence * 100).toFixed(1)

  return (
    <div className="space-y-6 fade-in-up">
      <div className={`glass-card p-7 bg-gradient-to-br ${isFake ? 'from-red-500/15 to-red-600/5 border-red-500/20' : 'from-emerald-500/15 to-emerald-600/5 border-emerald-500/20'}`}>
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
          <div>
            <p className="text-gray-400 text-xs uppercase tracking-wider mb-2">Prediction Result</p>
            <span className={`inline-block px-6 py-2 rounded-full text-sm font-bold border ${isFake ? 'bg-red-500/10 text-red-400 border-red-500/25' : 'bg-emerald-500/10 text-emerald-400 border-emerald-500/25'}`}>
              {isFake ? '🚫 FAKE NEWS' : '✅ REAL NEWS'}
            </span>
          </div>
          <div className="sm:text-right">
            <p className="text-gray-400 text-xs uppercase tracking-wider mb-1">Confidence</p>
            <p className={`text-3xl font-bold ${isFake ? 'text-red-400' : 'text-emerald-400'}`}>{confidence}%</p>
          </div>
        </div>
        <div className="mt-6">
          <div className="w-full bg-white/5 rounded-full h-3 overflow-hidden">
            <div className={`h-full rounded-full transition-all duration-1000 ease-out bg-gradient-to-r ${isFake ? 'from-red-500 to-red-600' : 'from-emerald-500 to-emerald-600'}`} style={{ width: `${confidence}%` }} />
          </div>
          <div className="flex justify-between mt-1.5">
            <span className="text-[10px] text-gray-500">0%</span>
            <span className="text-[10px] text-gray-500">100%</span>
          </div>
        </div>
      </div>

      <div className="glass-card p-7">
        <h3 className="text-white font-semibold text-sm mb-4">Analysis Breakdown</h3>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {(isFake
            ? [
                { label: 'Linguistic Pattern', value: 'Sensational & emotional language' },
                { label: 'Source Attribution', value: 'Lacks credible sources' },
                { label: 'Writing Style', value: 'Exaggerated & clickbait-style' },
                { label: 'Factual Consistency', value: 'Low' },
              ]
            : [
                { label: 'Linguistic Pattern', value: 'Measured & objective tone' },
                { label: 'Source Attribution', value: 'Contains source references' },
                { label: 'Writing Style', value: 'Professional journalism style' },
                { label: 'Factual Consistency', value: 'High' },
              ]
          ).map((point, i) => (
            <div key={i} className="bg-white/5 rounded-xl p-4 border border-white/5">
              <p className="text-gray-400 text-xs mb-1">{point.label}</p>
              <p className={`text-sm font-medium ${isFake ? 'text-red-400' : 'text-emerald-400'}`}>{point.value}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
