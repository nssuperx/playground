// Nは基底のサイズ（例: 8）
float N = 8;

float2 base_pos;

float4 main(float2 uv : TEXCOORD0) : SV_TARGET
{
    // 例えば8x8のDCT基底を想定50
    // uvは0.0から1.0の範囲
    
    // ピクセル座標に変換 (0 to N-1)
    float x = floor(uv.x * N);
    float y = floor(uv.y * N);

    // どのDCT基底を生成するかを指定 (例: u=1, v=2の基底)
    float u_basis = base_pos.x;
    float v_basis = base_pos.y;

    // DCT基底関数の計算 (正規化係数は省略)
    float val = cos(((2.0 * x + 1.0) * u_basis * 3.1415926535) / (2.0 * N)) *
                cos(((2.0 * y + 1.0) * v_basis * 3.1415926535) / (2.0 * N));

    // 値を色にマッピング (例: -1.0から1.0の値を0.0から1.0のグレースケールに)
    float color = (val + 1.0) / 2.0;

    return float4(color, color, color, 1.0);
}
