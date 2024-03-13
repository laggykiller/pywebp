from typing import Any, Callable, overload, Literal, Tuple, Union

class Pointer[O]: ...

class ffi:
    NULL: Pointer[None]

    @staticmethod
    @overload
    def new(ctype: Literal["WebPData*"]) -> lib.WebPDataPointer: ...
    
    @staticmethod
    @overload
    def new(ctype: Literal["WebPMemoryWriter*"]) -> lib.WebPMemoryWriterPointer: ...

    @staticmethod
    @overload
    def new(ctype: Literal["WebPPicture*"]) -> lib.WebPPicturePointer: ...

    @staticmethod
    @overload
    def new(ctype: Literal["WebPDecoderConfig*"]) -> lib.WebPDecoderConfigPointer: ...

    @staticmethod
    @overload
    def new(ctype: Literal["WebPAnimEncoderOptions*"]) -> lib.WebPAnimEncoderOptionsPointer: ...

    @staticmethod
    @overload
    def new(ctype: Literal["WebPAnimDecoderOptions*"]) -> lib.WebPAnimDecoderOptionsPointer: ...

    @staticmethod
    @overload
    def new(ctype: Literal["WebPAnimInfo*"]) -> lib.WebPAnimInfoPointer: ...

    @staticmethod
    @overload
    def new(ctype: str) -> Any: ...

    @staticmethod
    def cast(c_type: str, value: Any) -> Any: ...

    @staticmethod
    def addressof(cdata: Any, *fields_or_indexes: str) -> Any: ...

    @staticmethod
    def buffer(cdata: Any, size: int) -> bytes: ...

    @staticmethod
    def from_buffer(cdata: Any, require_writable: bool = False) -> bytes: ...

    @staticmethod
    def gc(cdata: Any, destructor: Callable[..., Any]) -> Any: ...

class lib:
    WEBP_PRESET_DEFAULT: int
    WEBP_PRESET_PICTURE: int
    WEBP_PRESET_PHOTO: int
    WEBP_PRESET_DRAWING: int
    WEBP_PRESET_ICON: int
    WEBP_PRESET_TEXT: int

    MODE_RGB: int
    MODE_RGBA: int
    MODE_BGR: int
    MODE_BGRA: int
    MODE_ARGB: int
    MODE_RGBA_4444: int
    MODE_RGB_565: int
    MODE_rgbA: int
    MODE_bgrA: int
    MODE_Argb: int
    MODE_rgbA_4444: int
    MODE_YUV: int
    MODE_YUVA: int
    MODE_LAST: int

    VP8_STATUS_OK: int
    VP8_STATUS_OUT_OF_MEMORY: int
    VP8_STATUS_INVALID_PARAM: int
    VP8_STATUS_BITSTREAM_ERROR: int
    VP8_STATUS_UNSUPPORTED_FEATURE: int
    VP8_STATUS_SUSPENDED: int
    VP8_STATUS_USER_ABORT: int
    VP8_STATUS_NOT_ENOUGH_DATA: int

    class WebPData:
        bytes: int
        size: int

    class WebPPicture:
        use_argb: int
        width: int
        height: int
        writer: Callable[[int, int, lib.WebPPicture], int]
        custom_ptr: None

    class WebPRGBABuffer:
        rgba: int
        stride: int
        size: int

    class WebPYUVABuffer:
        y: int
        u: int
        v: int
        a: int
        y_stride: int
        u_stride: int
        v_stride: int
        a_stride: int
        y_size: int
        u_size: int
        v_size: int
        a_size: int

    class WebPBitstreamFeatures:
        width: int
        height: int
        has_alpha: int
        has_animation: int
        format: int

    class WebPDecBuffer:
        colorspace: int
        width: int
        height: int
        is_external_memory: int
        u: Tuple[lib.WebPRGBABuffer, lib.WebPYUVABuffer]

    class WebPDecoderOptions:
        use_threads: int
        
    class WebPDecoderConfig:
        input: lib.WebPBitstreamFeatures
        output: lib.WebPDecBuffer
        options: lib.WebPDecoderOptions

    class WebPConfig:
        lossless: int
        quality: float
        method: int

    class WebPMemoryWriter:
        mem: int
        size: int

    class WebPAnimEncoderOptions:
        minimize_size: int
        kmin: int
        kmax: int
        allow_mixed: int
        verbose: int

    class WebPAnimDecoderOptions:
        color_mode: int
        use_threads: int

    class WebPAnimInfo:
        canvas_width: int
        canvas_height: int
        loop_count: int
        bgcolor: int
        frame_count: int

    class WebPMux: ...
    class WebPAnimEncoder: ...
    class WebPAnimDecoder: ...

    class WebPDataPointer(WebPData): ...
    class WebPMemoryWriterPointer(WebPMemoryWriter): ...
    class WebPPicturePointer(WebPPicture): ...
    class WebPDecoderConfigPointer(WebPDecoderConfig): ...
    class WebPAnimEncoderOptionsPointer(WebPAnimEncoderOptions): ...
    class WebPAnimDecoderOptionsPointer(WebPAnimDecoderOptions): ...
    class WebPAnimInfoPointer(WebPAnimInfo): ...

    @staticmethod
    def WebPPictureInit(picture: WebPPicturePointer) -> int: ...

    @staticmethod
    def WebPPictureAlloc(picture: WebPPicturePointer) -> int: ...

    @staticmethod
    def WebPPictureImportRGB(picture: WebPPicturePointer, rgb: Pointer[int], rgb_stride: int) -> int: ...

    @staticmethod
    def WebPPictureImportRGBA(picture: WebPPicturePointer, rgba: Pointer[int], rgba_stride: int) -> int: ...

    @staticmethod
    def WebPPictureFree(picture: WebPPicturePointer) -> None: ...

    @staticmethod
    def WebPInitDecoderConfig(config: WebPDecoderConfigPointer) -> int: ...

    @staticmethod
    def WebPGetFeatures(data: Pointer[int], data_size: int, features: Pointer[WebPBitstreamFeatures]) -> int: ...

    @staticmethod
    def WebPDecode(data: Pointer[int], data_size: int, config: WebPDecoderConfigPointer) -> int: ...

    @staticmethod
    def WebPFreeDecBuffer(buffer: Pointer[WebPDecBuffer]) -> None: ...

    @staticmethod
    def WebPConfigPreset(config: Pointer[WebPConfig], preset: int, quality: float) -> int: ...

    @staticmethod
    def WebPConfigLosslessPreset(config: Pointer[WebPConfig], level: int) -> int: ...

    @staticmethod
    def WebPValidateConfig(ptr: Pointer[WebPConfig]) -> int: ...

    @staticmethod
    def WebPEncode(config: Pointer[WebPConfig], picture: WebPPicturePointer) -> int: ...

    @staticmethod
    def WebPMemoryWriterInit(writer: WebPMemoryWriterPointer) -> None: ...

    @staticmethod
    def WebPMemoryWrite(data: Pointer[int], data_sie: int, picture: WebPPicturePointer) -> None: ...

    @staticmethod
    def WebPMemoryWriterClear(writer: WebPMemoryWriterPointer) -> None: ...

    @staticmethod
    def WebPFree(ptr: Pointer[None]) -> None: ...

    @staticmethod
    def WebPDataInit(webp_data: WebPDataPointer) -> None: ...

    @staticmethod
    def WebPDataClear(webp_data: WebPDataPointer) -> None: ...

    @staticmethod
    def WebPAnimEncoderOptionsInit(enc_options: WebPAnimEncoderOptionsPointer) -> int: ...

    @staticmethod
    def WebPAnimEncoderNew(width: int, height: int, enc_options: WebPAnimEncoderOptionsPointer) -> WebPAnimEncoder: ...

    @staticmethod
    def WebPAnimEncoderAdd(enc: Pointer[WebPAnimEncoder], frame: Union[Pointer[None], WebPPicturePointer], timestamp_ms: int, config: Union[Pointer[None], Pointer[WebPConfig]]) -> int: ...

    @staticmethod
    def WebPAnimEncoderAssemble(enc: WebPAnimEncoder, webp_data: WebPData) -> int: ...

    @staticmethod
    def WebPAnimEncoderDelete(enc: WebPAnimEncoder) -> None: ...

    @staticmethod
    def WebPAnimDecoderOptionsInit(dec_options: WebPAnimDecoderOptionsPointer) -> int: ...

    @staticmethod
    def WebPAnimDecoderNew(webp_data: WebPData, dec_options: WebPAnimDecoderOptionsPointer) -> Pointer[WebPAnimDecoder]: ...

    @staticmethod
    def WebPAnimDecoderGetInfo(dec: Union[Pointer[None], Pointer[WebPAnimDecoder]], info: WebPAnimInfo) -> int: ...

    @staticmethod
    def WebPAnimDecoderHasMoreFrames(dec: Pointer[WebPAnimDecoder]) -> int: ...

    @staticmethod
    def WebPAnimDecoderGetNext(dec: Pointer[WebPAnimDecoder], buf: Pointer[Pointer[int]], timestamp: int) -> int: ...

    @staticmethod
    def WebPAnimDecoderReset(dec: Pointer[WebPAnimDecoder]) -> None: ...

    @staticmethod
    def WebPAnimDecoderDelete(dec: Pointer[WebPAnimDecoder]) -> None: ...