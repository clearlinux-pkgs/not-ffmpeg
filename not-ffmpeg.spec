#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : not-ffmpeg
Version  : 4.2.1.reduced
Release  : 42
URL      : http://localhost/cgit/projects/ffmpeg/snapshot/ffmpeg-4.2.1-reduced.tar.xz
Source0  : http://localhost/cgit/projects/ffmpeg/snapshot/ffmpeg-4.2.1-reduced.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1 LGPL-3.0
Requires: not-ffmpeg-bin = %{version}-%{release}
Requires: not-ffmpeg-data = %{version}-%{release}
Requires: not-ffmpeg-lib = %{version}-%{release}
Requires: not-ffmpeg-license = %{version}-%{release}
BuildRequires : gmp-dev
BuildRequires : libass-dev
BuildRequires : libtheora-dev
BuildRequires : pkgconfig(dav1d)
BuildRequires : pkgconfig(libmfx)
BuildRequires : pkgconfig(libv4l2)
BuildRequires : pkgconfig(libva)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(sdl2)
BuildRequires : pkgconfig(vorbis)
BuildRequires : pkgconfig(vpx)
BuildRequires : rtmpdump-dev
BuildRequires : util-linux
Patch1: 0001-configure-do-not-die-if-unknown-option-is-found.patch
Patch2: 0001-not-ffmpeg-fixes-to-compilation-for-n-4.2.1-version.patch
Patch3: 0001-not-ffmpeg-enable-h264_qsv-encoder-and-decoder.patch
Patch4: 0001-add-fixes-for-demuxers-dnxhd-to-enable-mp4.patch
Patch5: 0005-lavx_qsv-Fix_MSDK_initialization_failure_in_system_memory.patch
Patch6: CVE-2019-15942.patch
Patch7: CVE-2020-12284.patch
Patch8: CVE-2020-13904.patch

%description
FFmpeg is a collection of libraries and tools to process multimedia content
such as audio, video, subtitles and related metadata.

%package bin
Summary: bin components for the not-ffmpeg package.
Group: Binaries
Requires: not-ffmpeg-data = %{version}-%{release}
Requires: not-ffmpeg-license = %{version}-%{release}

%description bin
bin components for the not-ffmpeg package.


%package data
Summary: data components for the not-ffmpeg package.
Group: Data

%description data
data components for the not-ffmpeg package.


%package dev
Summary: dev components for the not-ffmpeg package.
Group: Development
Requires: not-ffmpeg-lib = %{version}-%{release}
Requires: not-ffmpeg-bin = %{version}-%{release}
Requires: not-ffmpeg-data = %{version}-%{release}
Provides: not-ffmpeg-devel = %{version}-%{release}
Requires: not-ffmpeg = %{version}-%{release}

%description dev
dev components for the not-ffmpeg package.


%package lib
Summary: lib components for the not-ffmpeg package.
Group: Libraries
Requires: not-ffmpeg-data = %{version}-%{release}
Requires: not-ffmpeg-license = %{version}-%{release}

%description lib
lib components for the not-ffmpeg package.


%package license
Summary: license components for the not-ffmpeg package.
Group: Default

%description license
license components for the not-ffmpeg package.


%prep
%setup -q -n ffmpeg-4.2.1-reduced
cd %{_builddir}/ffmpeg-4.2.1-reduced
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600109251
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static --extra-ldflags='-ldl' \
--disable-everything \
--enable-avcodec \
--enable-avformat \
--enable-avutil \
--enable-avdevice \
--enable-rdft \
--enable-pixelutils \
--enable-libvorbis \
--enable-libvpx \
--enable-muxer="crc,image2,jpeg,ogg,md5,nut,webm,webm_chunk,webm_dash_manifest,rawvideo,ivf,null,wav,framecrc,rtp,rtsp,ass,webvtt,mjpeg,framehash,hash,mp4,avi" \
--enable-bsf="mp3_header_decompress,vp9_superframe" \
--enable-demuxer="mjpeg,image2,webm_dash_manifest,ogg,matroska,mp3,pcm_s16le,rawvideo,wav,mov,ivf,rtp,rtsp,flv,ass,subviewer,subviewer1,webvtt,h264,dnxhd,avi" \
--enable-decoder="rawvideo,libvorbis,mjpeg,jpeg,opus,mp3,pcm_u8,pcm_s16le,pcm_s24le,pcm_s32le,pcm_f32le,pcm_s16be,pcm_s24be,pcm_mulaw,pcm_alaw,pcm_u24le,pcm_u32be,pcm_u32le,pgm,pgmyuv,libvpx_vp8,vp8_qsv,vp8,libvpx_vp9,vp9,tiff,bmp,wavpack,ass,saa,subviewer,subviewer1,webvtt,h264_qsv,yuv4,libdav1d" \
--enable-encoder="rawvideo,wrapped_avframe,libvorbis,opus,yuv4,tiff,bmp,libvpx_vp8,vp8_vaapi,libvpx_vp9,vp9_vaapi,mjpeg_vaapi,pcm_u8,pcm_s16le,pcm_s24le,pcm_s32le,pcm_f32le,pcm_s16be,pcm_s24be,pcm_mulaw,pcm_alaw,pcm_u24le,pcm_u32be,pcm_u32le,ass,ssa,webvtt,mjpeg_qsv,h264_qsv,libtheora" \
--enable-hwaccel="vp8_vaapi,vp9_vaapi,mjpeg_vaapi" \
--enable-parser="opus,libvorbis,vp3,vp8,vp9,mjpeg" \
--enable-protocol="file,md5,pipe,rtp,tcp,http,https,httpproxy,ftp,librtmp,librtmpe,librtmps,librtmpt,librtmpte,rtmpe,rtmps,rtmpt,rtmpte,rtmpts" \
--enable-filter="acopy,aresample,ashowinfo,aselect,asetpts,copy,denoise_vaapi,deinterlace_vaapi,hwmap,hwupload,hwdownload,pixdesctest,procamp_vaapi,scale,scale_vaapi,sharpness_vaapi,showinfo,color,format,subtitles,select,setpts" \
--disable-error-resilience \
--enable-pic \
--enable-shared \
--enable-swscale \
--enable-avfilter \
--enable-vaapi \
--enable-libmfx \
--disable-xvmc \
--disable-doc \
--disable-htmlpages \
--enable-version3 \
--disable-mmx \
--disable-mmxext \
--disable-programs \
--enable-ffmpeg \
--enable-ffplay \
--enable-sdl2 \
--enable-network \
--enable-openssl \
--enable-librtmp \
--enable-libv4l2 \
--enable-indev="v4l2" \
--enable-outdev="sdl2" \
--enable-libass \
--enable-libtheora \
--enable-libdav1d
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1600109251
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/not-ffmpeg
cp %{_builddir}/ffmpeg-4.2.1-reduced/COPYING.LGPLv2.1 %{buildroot}/usr/share/package-licenses/not-ffmpeg/37d2f1d62fec4da0caf06e5da21afc3521b597aa
cp %{_builddir}/ffmpeg-4.2.1-reduced/COPYING.LGPLv3 %{buildroot}/usr/share/package-licenses/not-ffmpeg/f45ee1c765646813b442ca58de72e20a64a7ddba
cp %{_builddir}/ffmpeg-4.2.1-reduced/LICENSE.md %{buildroot}/usr/share/package-licenses/not-ffmpeg/9a405073a73ffff7c35e7ad37a3d6afbf99e1c6a
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ffmpeg
/usr/bin/ffplay

%files data
%defattr(-,root,root,-)
/usr/share/examples/Makefile
/usr/share/examples/README
/usr/share/examples/avio_dir_cmd.c
/usr/share/examples/avio_reading.c
/usr/share/examples/decode_audio.c
/usr/share/examples/decode_video.c
/usr/share/examples/demuxing_decoding.c
/usr/share/examples/encode_audio.c
/usr/share/examples/encode_video.c
/usr/share/examples/extract_mvs.c
/usr/share/examples/filter_audio.c
/usr/share/examples/filtering_audio.c
/usr/share/examples/filtering_video.c
/usr/share/examples/http_multiclient.c
/usr/share/examples/hw_decode.c
/usr/share/examples/metadata.c
/usr/share/examples/muxing.c
/usr/share/examples/qsvdec.c
/usr/share/examples/remuxing.c
/usr/share/examples/resampling_audio.c
/usr/share/examples/scaling_video.c
/usr/share/examples/transcode_aac.c
/usr/share/examples/transcoding.c
/usr/share/examples/vaapi_encode.c
/usr/share/examples/vaapi_transcode.c
/usr/share/ffprobe.xsd
/usr/share/libvpx-1080p.ffpreset
/usr/share/libvpx-1080p50_60.ffpreset
/usr/share/libvpx-360p.ffpreset
/usr/share/libvpx-720p.ffpreset
/usr/share/libvpx-720p50_60.ffpreset

%files dev
%defattr(-,root,root,-)
/usr/include/libavcodec/ac3_parser.h
/usr/include/libavcodec/adts_parser.h
/usr/include/libavcodec/avcodec.h
/usr/include/libavcodec/avdct.h
/usr/include/libavcodec/avfft.h
/usr/include/libavcodec/d3d11va.h
/usr/include/libavcodec/dirac.h
/usr/include/libavcodec/dv_profile.h
/usr/include/libavcodec/dxva2.h
/usr/include/libavcodec/jni.h
/usr/include/libavcodec/mediacodec.h
/usr/include/libavcodec/qsv.h
/usr/include/libavcodec/vaapi.h
/usr/include/libavcodec/vdpau.h
/usr/include/libavcodec/version.h
/usr/include/libavcodec/videotoolbox.h
/usr/include/libavcodec/vorbis_parser.h
/usr/include/libavcodec/xvmc.h
/usr/include/libavdevice/avdevice.h
/usr/include/libavdevice/version.h
/usr/include/libavfilter/avfilter.h
/usr/include/libavfilter/buffersink.h
/usr/include/libavfilter/buffersrc.h
/usr/include/libavfilter/version.h
/usr/include/libavformat/avformat.h
/usr/include/libavformat/avio.h
/usr/include/libavformat/version.h
/usr/include/libavutil/adler32.h
/usr/include/libavutil/aes.h
/usr/include/libavutil/aes_ctr.h
/usr/include/libavutil/attributes.h
/usr/include/libavutil/audio_fifo.h
/usr/include/libavutil/avassert.h
/usr/include/libavutil/avconfig.h
/usr/include/libavutil/avstring.h
/usr/include/libavutil/avutil.h
/usr/include/libavutil/base64.h
/usr/include/libavutil/blowfish.h
/usr/include/libavutil/bprint.h
/usr/include/libavutil/bswap.h
/usr/include/libavutil/buffer.h
/usr/include/libavutil/camellia.h
/usr/include/libavutil/cast5.h
/usr/include/libavutil/channel_layout.h
/usr/include/libavutil/common.h
/usr/include/libavutil/cpu.h
/usr/include/libavutil/crc.h
/usr/include/libavutil/des.h
/usr/include/libavutil/dict.h
/usr/include/libavutil/display.h
/usr/include/libavutil/downmix_info.h
/usr/include/libavutil/encryption_info.h
/usr/include/libavutil/error.h
/usr/include/libavutil/eval.h
/usr/include/libavutil/ffversion.h
/usr/include/libavutil/fifo.h
/usr/include/libavutil/file.h
/usr/include/libavutil/frame.h
/usr/include/libavutil/hash.h
/usr/include/libavutil/hdr_dynamic_metadata.h
/usr/include/libavutil/hmac.h
/usr/include/libavutil/hwcontext.h
/usr/include/libavutil/hwcontext_cuda.h
/usr/include/libavutil/hwcontext_d3d11va.h
/usr/include/libavutil/hwcontext_drm.h
/usr/include/libavutil/hwcontext_dxva2.h
/usr/include/libavutil/hwcontext_mediacodec.h
/usr/include/libavutil/hwcontext_qsv.h
/usr/include/libavutil/hwcontext_vaapi.h
/usr/include/libavutil/hwcontext_vdpau.h
/usr/include/libavutil/hwcontext_videotoolbox.h
/usr/include/libavutil/imgutils.h
/usr/include/libavutil/intfloat.h
/usr/include/libavutil/intreadwrite.h
/usr/include/libavutil/lfg.h
/usr/include/libavutil/log.h
/usr/include/libavutil/lzo.h
/usr/include/libavutil/macros.h
/usr/include/libavutil/mastering_display_metadata.h
/usr/include/libavutil/mathematics.h
/usr/include/libavutil/md5.h
/usr/include/libavutil/mem.h
/usr/include/libavutil/motion_vector.h
/usr/include/libavutil/murmur3.h
/usr/include/libavutil/opt.h
/usr/include/libavutil/parseutils.h
/usr/include/libavutil/pixdesc.h
/usr/include/libavutil/pixelutils.h
/usr/include/libavutil/pixfmt.h
/usr/include/libavutil/random_seed.h
/usr/include/libavutil/rational.h
/usr/include/libavutil/rc4.h
/usr/include/libavutil/replaygain.h
/usr/include/libavutil/ripemd.h
/usr/include/libavutil/samplefmt.h
/usr/include/libavutil/sha.h
/usr/include/libavutil/sha512.h
/usr/include/libavutil/spherical.h
/usr/include/libavutil/stereo3d.h
/usr/include/libavutil/tea.h
/usr/include/libavutil/threadmessage.h
/usr/include/libavutil/time.h
/usr/include/libavutil/timecode.h
/usr/include/libavutil/timestamp.h
/usr/include/libavutil/tree.h
/usr/include/libavutil/twofish.h
/usr/include/libavutil/tx.h
/usr/include/libavutil/version.h
/usr/include/libavutil/xtea.h
/usr/include/libswresample/swresample.h
/usr/include/libswresample/version.h
/usr/include/libswscale/swscale.h
/usr/include/libswscale/version.h
/usr/lib64/libavcodec.so
/usr/lib64/libavdevice.so
/usr/lib64/libavfilter.so
/usr/lib64/libavformat.so
/usr/lib64/libavutil.so
/usr/lib64/libswresample.so
/usr/lib64/libswscale.so
/usr/lib64/pkgconfig/libavcodec.pc
/usr/lib64/pkgconfig/libavdevice.pc
/usr/lib64/pkgconfig/libavfilter.pc
/usr/lib64/pkgconfig/libavformat.pc
/usr/lib64/pkgconfig/libavutil.pc
/usr/lib64/pkgconfig/libswresample.pc
/usr/lib64/pkgconfig/libswscale.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libavcodec.so.58
/usr/lib64/libavcodec.so.58.54.100
/usr/lib64/libavdevice.so.58
/usr/lib64/libavdevice.so.58.8.100
/usr/lib64/libavfilter.so.7
/usr/lib64/libavfilter.so.7.57.100
/usr/lib64/libavformat.so.58
/usr/lib64/libavformat.so.58.29.100
/usr/lib64/libavutil.so.56
/usr/lib64/libavutil.so.56.31.100
/usr/lib64/libswresample.so.3
/usr/lib64/libswresample.so.3.5.100
/usr/lib64/libswscale.so.5
/usr/lib64/libswscale.so.5.5.100

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/not-ffmpeg/37d2f1d62fec4da0caf06e5da21afc3521b597aa
/usr/share/package-licenses/not-ffmpeg/9a405073a73ffff7c35e7ad37a3d6afbf99e1c6a
/usr/share/package-licenses/not-ffmpeg/f45ee1c765646813b442ca58de72e20a64a7ddba
