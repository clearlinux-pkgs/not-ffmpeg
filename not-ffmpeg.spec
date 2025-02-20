#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v21
# autospec commit: fbbd4e3
#
# Source0 file verified with key 0xB4322F04D67658D8 (ffmpeg-devel@ffmpeg.org)
#
Name     : not-ffmpeg
Version  : 7.1
Release  : 98
URL      : https://ffmpeg.org/releases/ffmpeg-7.1.tar.gz
Source0  : https://ffmpeg.org/releases/ffmpeg-7.1.tar.gz
Source1  : https://github.com/intel/cartwheel-ffmpeg/archive/2024q3/cartwheel-ffmpeg-2024q3.tar.gz
Source2  : https://ffmpeg.org/releases/ffmpeg-7.1.tar.gz.asc
Source3  : B4322F04D67658D8.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0
Requires: not-ffmpeg-bin = %{version}-%{release}
Requires: not-ffmpeg-data = %{version}-%{release}
Requires: not-ffmpeg-lib = %{version}-%{release}
Requires: not-ffmpeg-license = %{version}-%{release}
Requires: not-ffmpeg-man = %{version}-%{release}
BuildRequires : Vulkan-Headers-dev
BuildRequires : buildreq-configure
BuildRequires : gmp-dev
BuildRequires : gnupg
BuildRequires : ladspa_sdk-dev
BuildRequires : libass-dev
BuildRequires : libtheora-dev
BuildRequires : nasm
BuildRequires : pkgconfig(SvtAv1Enc)
BuildRequires : pkgconfig(aom)
BuildRequires : pkgconfig(dav1d)
BuildRequires : pkgconfig(jack)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libmfx)
BuildRequires : pkgconfig(libopenjp2)
BuildRequires : pkgconfig(libopenmpt)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(librist)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(libssh)
BuildRequires : pkgconfig(libv4l2)
BuildRequires : pkgconfig(libva)
BuildRequires : pkgconfig(libwebp)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(opus)
BuildRequires : pkgconfig(sdl2)
BuildRequires : pkgconfig(speex)
BuildRequires : pkgconfig(srt)
BuildRequires : pkgconfig(vapoursynth-script)
BuildRequires : pkgconfig(vidstab)
BuildRequires : pkgconfig(vorbis)
BuildRequires : pkgconfig(vpx)
BuildRequires : pkgconfig(x264)
BuildRequires : pkgconfig(x265)
BuildRequires : pkgconfig(zimg)
BuildRequires : rtmpdump-dev
BuildRequires : xvidcore-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-configure-do-not-die-if-unknown-option-is-found.patch

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


%package man
Summary: man components for the not-ffmpeg package.
Group: Default

%description man
man components for the not-ffmpeg package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE3}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE2} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) B4322F04D67658D8' gpg.status
%setup -q -n ffmpeg-7.1
cd %{_builddir}
tar xf %{_sourcedir}/cartwheel-ffmpeg-2024q3.tar.gz
cd %{_builddir}/ffmpeg-7.1
mkdir -p ../cartwheel-ffmpeg
cp -r %{_builddir}/cartwheel-ffmpeg-2024q3/. %{_builddir}/ffmpeg-7.1/../cartwheel-ffmpeg
%patch -P 1 -p1
pushd ..
cp -a ffmpeg-7.1 buildavx2
popd
pushd ..
cp -a ffmpeg-7.1 buildavx512
popd
pushd ..
cp -a ffmpeg-7.1 buildapx
popd

%build
## build_prepend content
for patch in ../cartwheel-ffmpeg/patches/*.patch; do
patch -p1 < ${patch}
done
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1740081303
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --disable-debug \
--disable-static \
--disable-stripping \
--enable-lto \
--enable-fontconfig \
--enable-gmp \
--enable-gnutls \
--enable-gpl \
--enable-ladspa \
--enable-libaom \
--enable-libass \
--enable-libdav1d \
--enable-libdrm \
--enable-libfreetype \
--enable-libfribidi \
--enable-libjack \
--enable-libmfx \
--enable-libopenjpeg \
--enable-libopenmpt \
--enable-libopus \
--enable-libpulse \
--enable-librist \
--enable-librsvg \
--enable-libspeex \
--enable-libsrt \
--enable-libssh \
--enable-libsvtav1 \
--enable-libtheora \
--enable-libv4l2 \
--enable-libvidstab \
--enable-libvorbis \
--enable-libvpx \
--enable-libwebp \
--enable-libx264 \
--enable-libx265 \
--enable-libxcb \
--enable-libxml2 \
--enable-libxvid \
--enable-libzimg \
--enable-shared \
--enable-vapoursynth \
--enable-version3 \
--enable-vulkan \
--disable-asm
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
## build_prepend content
for patch in ../cartwheel-ffmpeg/patches/*.patch; do
patch -p1 < ${patch}
done
## build_prepend end
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --disable-debug \
--disable-static \
--disable-stripping \
--enable-lto \
--enable-fontconfig \
--enable-gmp \
--enable-gnutls \
--enable-gpl \
--enable-ladspa \
--enable-libaom \
--enable-libass \
--enable-libdav1d \
--enable-libdrm \
--enable-libfreetype \
--enable-libfribidi \
--enable-libjack \
--enable-libmfx \
--enable-libopenjpeg \
--enable-libopenmpt \
--enable-libopus \
--enable-libpulse \
--enable-librist \
--enable-librsvg \
--enable-libspeex \
--enable-libsrt \
--enable-libssh \
--enable-libsvtav1 \
--enable-libtheora \
--enable-libv4l2 \
--enable-libvidstab \
--enable-libvorbis \
--enable-libvpx \
--enable-libwebp \
--enable-libx264 \
--enable-libx265 \
--enable-libxcb \
--enable-libxml2 \
--enable-libxvid \
--enable-libzimg \
--enable-shared \
--enable-vapoursynth \
--enable-version3 \
--enable-vulkan \
--disable-asm
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
## build_prepend content
for patch in ../cartwheel-ffmpeg/patches/*.patch; do
patch -p1 < ${patch}
done
## build_prepend end
GOAMD64=v4
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v4 -mprefer-vector-width=256 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v4 "
%configure --disable-static --disable-debug \
--disable-static \
--disable-stripping \
--enable-lto \
--enable-fontconfig \
--enable-gmp \
--enable-gnutls \
--enable-gpl \
--enable-ladspa \
--enable-libaom \
--enable-libass \
--enable-libdav1d \
--enable-libdrm \
--enable-libfreetype \
--enable-libfribidi \
--enable-libjack \
--enable-libmfx \
--enable-libopenjpeg \
--enable-libopenmpt \
--enable-libopus \
--enable-libpulse \
--enable-librist \
--enable-librsvg \
--enable-libspeex \
--enable-libsrt \
--enable-libssh \
--enable-libsvtav1 \
--enable-libtheora \
--enable-libv4l2 \
--enable-libvidstab \
--enable-libvorbis \
--enable-libvpx \
--enable-libwebp \
--enable-libx264 \
--enable-libx265 \
--enable-libxcb \
--enable-libxml2 \
--enable-libxvid \
--enable-libzimg \
--enable-shared \
--enable-vapoursynth \
--enable-version3 \
--enable-vulkan \
--disable-asm
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildapx/
## build_prepend content
for patch in ../cartwheel-ffmpeg/patches/*.patch; do
patch -p1 < ${patch}
done
## build_prepend end
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --host=x86_64-clr-linux-gnu --disable-static --disable-debug \
--disable-static \
--disable-stripping \
--enable-lto \
--enable-fontconfig \
--enable-gmp \
--enable-gnutls \
--enable-gpl \
--enable-ladspa \
--enable-libaom \
--enable-libass \
--enable-libdav1d \
--enable-libdrm \
--enable-libfreetype \
--enable-libfribidi \
--enable-libjack \
--enable-libmfx \
--enable-libopenjpeg \
--enable-libopenmpt \
--enable-libopus \
--enable-libpulse \
--enable-librist \
--enable-librsvg \
--enable-libspeex \
--enable-libsrt \
--enable-libssh \
--enable-libsvtav1 \
--enable-libtheora \
--enable-libv4l2 \
--enable-libvidstab \
--enable-libvorbis \
--enable-libvpx \
--enable-libwebp \
--enable-libx264 \
--enable-libx265 \
--enable-libxcb \
--enable-libxml2 \
--enable-libxvid \
--enable-libzimg \
--enable-shared \
--enable-vapoursynth \
--enable-version3 \
--enable-vulkan \
--disable-asm
make  %{?_smp_mflags}
popd
%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1740081303
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/not-ffmpeg
cp %{_builddir}/cartwheel-ffmpeg-2024q3/LICENSE %{buildroot}/usr/share/package-licenses/not-ffmpeg/b386b371ce94933e63ced1052aa72a60da5485ff || :
cp %{_builddir}/ffmpeg-%{version}/COPYING.GPLv2 %{buildroot}/usr/share/package-licenses/not-ffmpeg/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/ffmpeg-%{version}/COPYING.GPLv3 %{buildroot}/usr/share/package-licenses/not-ffmpeg/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/ffmpeg-%{version}/COPYING.LGPLv2.1 %{buildroot}/usr/share/package-licenses/not-ffmpeg/37d2f1d62fec4da0caf06e5da21afc3521b597aa || :
cp %{_builddir}/ffmpeg-%{version}/COPYING.LGPLv3 %{buildroot}/usr/share/package-licenses/not-ffmpeg/f45ee1c765646813b442ca58de72e20a64a7ddba || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v4
pushd ../buildavx512/
%make_install_v4
popd
GOAMD64=v3
pushd ../buildapx/
%make_install_va
popd
GOAMD64=v2
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/bin/ffmpeg
rm -f %{buildroot}*/usr/bin/ffplay
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/ffprobe
/V4/usr/bin/ffprobe
/VA/usr/bin/ffprobe
/usr/bin/ffprobe

%files data
%defattr(-,root,root,-)
/usr/share/examples/Makefile
/usr/share/examples/README
/usr/share/examples/avio_http_serve_files.c
/usr/share/examples/avio_list_dir.c
/usr/share/examples/avio_read_callback.c
/usr/share/examples/decode_audio.c
/usr/share/examples/decode_filter_audio.c
/usr/share/examples/decode_filter_video.c
/usr/share/examples/decode_video.c
/usr/share/examples/demux_decode.c
/usr/share/examples/encode_audio.c
/usr/share/examples/encode_video.c
/usr/share/examples/extract_mvs.c
/usr/share/examples/filter_audio.c
/usr/share/examples/hw_decode.c
/usr/share/examples/mux.c
/usr/share/examples/qsv_decode.c
/usr/share/examples/qsv_transcode.c
/usr/share/examples/remux.c
/usr/share/examples/resample_audio.c
/usr/share/examples/scale_video.c
/usr/share/examples/show_metadata.c
/usr/share/examples/transcode.c
/usr/share/examples/transcode_aac.c
/usr/share/examples/vaapi_decode.c
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
/usr/include/libavcodec/bsf.h
/usr/include/libavcodec/codec.h
/usr/include/libavcodec/codec_desc.h
/usr/include/libavcodec/codec_id.h
/usr/include/libavcodec/codec_par.h
/usr/include/libavcodec/d3d11va.h
/usr/include/libavcodec/defs.h
/usr/include/libavcodec/dirac.h
/usr/include/libavcodec/dv_profile.h
/usr/include/libavcodec/dxva2.h
/usr/include/libavcodec/jni.h
/usr/include/libavcodec/mediacodec.h
/usr/include/libavcodec/packet.h
/usr/include/libavcodec/qsv.h
/usr/include/libavcodec/vdpau.h
/usr/include/libavcodec/version.h
/usr/include/libavcodec/version_major.h
/usr/include/libavcodec/videotoolbox.h
/usr/include/libavcodec/vorbis_parser.h
/usr/include/libavdevice/avdevice.h
/usr/include/libavdevice/version.h
/usr/include/libavdevice/version_major.h
/usr/include/libavfilter/avfilter.h
/usr/include/libavfilter/buffersink.h
/usr/include/libavfilter/buffersrc.h
/usr/include/libavfilter/version.h
/usr/include/libavfilter/version_major.h
/usr/include/libavformat/avformat.h
/usr/include/libavformat/avio.h
/usr/include/libavformat/version.h
/usr/include/libavformat/version_major.h
/usr/include/libavutil/adler32.h
/usr/include/libavutil/aes.h
/usr/include/libavutil/aes_ctr.h
/usr/include/libavutil/ambient_viewing_environment.h
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
/usr/include/libavutil/csp.h
/usr/include/libavutil/des.h
/usr/include/libavutil/detection_bbox.h
/usr/include/libavutil/dict.h
/usr/include/libavutil/display.h
/usr/include/libavutil/dovi_meta.h
/usr/include/libavutil/downmix_info.h
/usr/include/libavutil/encryption_info.h
/usr/include/libavutil/error.h
/usr/include/libavutil/eval.h
/usr/include/libavutil/executor.h
/usr/include/libavutil/ffversion.h
/usr/include/libavutil/fifo.h
/usr/include/libavutil/file.h
/usr/include/libavutil/film_grain_params.h
/usr/include/libavutil/frame.h
/usr/include/libavutil/hash.h
/usr/include/libavutil/hdr_dynamic_metadata.h
/usr/include/libavutil/hdr_dynamic_vivid_metadata.h
/usr/include/libavutil/hmac.h
/usr/include/libavutil/hwcontext.h
/usr/include/libavutil/hwcontext_cuda.h
/usr/include/libavutil/hwcontext_d3d11va.h
/usr/include/libavutil/hwcontext_d3d12va.h
/usr/include/libavutil/hwcontext_drm.h
/usr/include/libavutil/hwcontext_dxva2.h
/usr/include/libavutil/hwcontext_mediacodec.h
/usr/include/libavutil/hwcontext_opencl.h
/usr/include/libavutil/hwcontext_qsv.h
/usr/include/libavutil/hwcontext_vaapi.h
/usr/include/libavutil/hwcontext_vdpau.h
/usr/include/libavutil/hwcontext_videotoolbox.h
/usr/include/libavutil/hwcontext_vulkan.h
/usr/include/libavutil/iamf.h
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
/usr/include/libavutil/sub_frame_metadata.h
/usr/include/libavutil/tea.h
/usr/include/libavutil/threadmessage.h
/usr/include/libavutil/time.h
/usr/include/libavutil/timecode.h
/usr/include/libavutil/timestamp.h
/usr/include/libavutil/tree.h
/usr/include/libavutil/twofish.h
/usr/include/libavutil/tx.h
/usr/include/libavutil/uuid.h
/usr/include/libavutil/version.h
/usr/include/libavutil/video_enc_params.h
/usr/include/libavutil/video_hint.h
/usr/include/libavutil/xtea.h
/usr/include/libpostproc/postprocess.h
/usr/include/libpostproc/version.h
/usr/include/libpostproc/version_major.h
/usr/include/libswresample/swresample.h
/usr/include/libswresample/version.h
/usr/include/libswresample/version_major.h
/usr/include/libswscale/swscale.h
/usr/include/libswscale/version.h
/usr/include/libswscale/version_major.h
/usr/lib64/libavcodec.so
/usr/lib64/libavdevice.so
/usr/lib64/libavfilter.so
/usr/lib64/libavformat.so
/usr/lib64/libavutil.so
/usr/lib64/libpostproc.so
/usr/lib64/libswresample.so
/usr/lib64/libswscale.so
/usr/lib64/pkgconfig/libavcodec.pc
/usr/lib64/pkgconfig/libavdevice.pc
/usr/lib64/pkgconfig/libavfilter.pc
/usr/lib64/pkgconfig/libavformat.pc
/usr/lib64/pkgconfig/libavutil.pc
/usr/lib64/pkgconfig/libpostproc.pc
/usr/lib64/pkgconfig/libswresample.pc
/usr/lib64/pkgconfig/libswscale.pc
/usr/share/man/man3/libavcodec.3
/usr/share/man/man3/libavdevice.3
/usr/share/man/man3/libavfilter.3
/usr/share/man/man3/libavformat.3
/usr/share/man/man3/libavutil.3
/usr/share/man/man3/libswresample.3
/usr/share/man/man3/libswscale.3

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libavcodec.so.61.19.100
/V3/usr/lib64/libavdevice.so.61.3.100
/V3/usr/lib64/libavfilter.so.10.4.100
/V3/usr/lib64/libavformat.so.61.7.100
/V3/usr/lib64/libavutil.so.59.39.100
/V3/usr/lib64/libpostproc.so.58.3.100
/V3/usr/lib64/libswresample.so.5.3.100
/V3/usr/lib64/libswscale.so.8.3.100
/V4/usr/lib64/libavcodec.so.61.19.100
/V4/usr/lib64/libavdevice.so.61.3.100
/V4/usr/lib64/libavfilter.so.10.4.100
/V4/usr/lib64/libavformat.so.61.7.100
/V4/usr/lib64/libavutil.so.59.39.100
/V4/usr/lib64/libpostproc.so.58.3.100
/V4/usr/lib64/libswresample.so.5.3.100
/V4/usr/lib64/libswscale.so.8.3.100
/VA/usr/lib64/libavcodec.so.61.19.100
/VA/usr/lib64/libavdevice.so.61.3.100
/VA/usr/lib64/libavfilter.so.10.4.100
/VA/usr/lib64/libavformat.so.61.7.100
/VA/usr/lib64/libavutil.so.59.39.100
/VA/usr/lib64/libpostproc.so.58.3.100
/VA/usr/lib64/libswresample.so.5.3.100
/VA/usr/lib64/libswscale.so.8.3.100
/usr/lib64/libavcodec.so.61
/usr/lib64/libavcodec.so.61.19.100
/usr/lib64/libavdevice.so.61
/usr/lib64/libavdevice.so.61.3.100
/usr/lib64/libavfilter.so.10
/usr/lib64/libavfilter.so.10.4.100
/usr/lib64/libavformat.so.61
/usr/lib64/libavformat.so.61.7.100
/usr/lib64/libavutil.so.59
/usr/lib64/libavutil.so.59.39.100
/usr/lib64/libpostproc.so.58
/usr/lib64/libpostproc.so.58.3.100
/usr/lib64/libswresample.so.5
/usr/lib64/libswresample.so.5.3.100
/usr/lib64/libswscale.so.8
/usr/lib64/libswscale.so.8.3.100

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/not-ffmpeg/37d2f1d62fec4da0caf06e5da21afc3521b597aa
/usr/share/package-licenses/not-ffmpeg/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/not-ffmpeg/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/not-ffmpeg/b386b371ce94933e63ced1052aa72a60da5485ff
/usr/share/package-licenses/not-ffmpeg/f45ee1c765646813b442ca58de72e20a64a7ddba

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ffmpeg-all.1
/usr/share/man/man1/ffmpeg-bitstream-filters.1
/usr/share/man/man1/ffmpeg-codecs.1
/usr/share/man/man1/ffmpeg-devices.1
/usr/share/man/man1/ffmpeg-filters.1
/usr/share/man/man1/ffmpeg-formats.1
/usr/share/man/man1/ffmpeg-protocols.1
/usr/share/man/man1/ffmpeg-resampler.1
/usr/share/man/man1/ffmpeg-scaler.1
/usr/share/man/man1/ffmpeg-utils.1
/usr/share/man/man1/ffmpeg.1
/usr/share/man/man1/ffplay-all.1
/usr/share/man/man1/ffplay.1
/usr/share/man/man1/ffprobe-all.1
/usr/share/man/man1/ffprobe.1
