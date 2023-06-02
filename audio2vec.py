import numpy as np
from pydub import AudioSegment

# 读取mp3文件
audio_file = AudioSegment.from_file("./手心的蔷薇.mp3", format="mp3")

# 获取采样率
sample_rate = audio_file.frame_rate

# 获取采样深度
sample_width = audio_file.sample_width

# 获取声道数
channels = audio_file.channels


# 打印文件信息
print(f"采样率：{sample_rate} Hz")
print(f"采样深度：{sample_width} Bytes")
print()
print(f"声道数：{channels}")

# 读取音频
samples = audio_file.get_array_of_samples()
print(len(samples))

# 剪切60s到65s的音频
sample_cut = samples[60 * sample_rate * 2 : 65 * sample_rate * 2]
sample_cut = np.array(sample_cut, dtype=np.int16)
print(f"sample_cut的长度是 {len(sample_cut)}")

fft_original = np.fft.fft(sample_cut)

# Thresholding
value = 5000  # 设定值
result_array = np.where(sample_cut > value, 1, 0)  # 判断并赋值为1或0

fft_threshold = np.fft.fft(value * result_array)  # 这里注意乘一个判决门限
