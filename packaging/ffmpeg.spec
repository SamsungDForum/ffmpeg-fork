Name:       ffmpeg
Summary:    ffmpeg tools
Version:    4.3.1
Release:    0
Group:      Multimedia/Libraries
URL:        https://ffmpeg.org
License:    LGPL-2.1+
Source0:    %{name}-%{version}.tar.gz

%description
ffmpeg tools

%package devel
Summary:    ffmpeg tools (devel)
Group:      Multimedia/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
ffmpeg library (devel)

%define SUFFIX -juvo
%define _rpm_strip_option --strip-all

%prep
%setup -q

export CONFIGURE_OPTIONS="--enable-shared    --disable-static   --disable-stripping \
--disable-version3  --disable-devices   --disable-nonfree --disable-gpl --disable-doc \
--disable-zlib    --disable-network \
--disable-avdevice \
--disable-bsfs      --disable-filters \
--enable-filter=buffer  --enable-filter=buffersink      --enable-filter=crop \
--enable-filter=hflip   --enable-filter=lut     --enable-filter=lutyuv \
--enable-filter=lutrgb  --enable-filter=overlay --enable-filter=scale \
--enable-filter=transpose       --enable-filter=unsharp --enable-filter=vflip \
--disable-protocols \
--disable-avresample \
--enable-protocol=file \
--disable-encoders \
--disable-muxers \
--disable-parsers \
--enable-parser=aac     --enable-parser=h264            --enable-parser=mpegaudio \
--enable-parser=h263    --enable-parser=mpeg4video      --enable-parser=mpegvideo \
--enable-parser=hevc \
--disable-demuxers \
--enable-demuxer=aac    --enable-demuxer=h264   --enable-demuxer=mpegts \
--enable-demuxer=amr    --enable-demuxer=m4v    --enable-demuxer=mpegtsraw \
--enable-demuxer=asf    --enable-demuxer=mmf    --enable-demuxer=mpegvideo \
--enable-demuxer=avi    --enable-demuxer=mov    --enable-demuxer=ogg \
--enable-demuxer=flac   --enable-demuxer=mp3    --enable-demuxer=wav \
--enable-demuxer=h263   --enable-demuxer=mpegps --enable-demuxer=matroska \
--enable-demuxer=dv		--enable-demuxer=flv	--enable-demuxer=rm \
--enable-demuxer=aiff	--enable-muxer=mpeg1video	--enable-muxer=mpeg2video	--enable-demuxer=hevc \
--disable-decoders \
--enable-decoder=alac   --enable-decoder=h264		--enable-decoder=wmv1 \
--enable-decoder=flac   --enable-decoder=mpeg4		--enable-decoder=wmv2 \
--enable-decoder=h263   --enable-decoder=mpegvideo	--enable-decoder=wmv3 \
--enable-decoder=vc1	--enable-decoder=flv 		--enable-decoder=rv40 \
--enable-decoder=h263i  --enable-decoder=theora  	--enable-decoder=mpeg1video	--enable-decoder=mpeg2video \
--enable-decoder=pcm_alaw  --enable-decoder=pcm_mulaw \
--enable-decoder=msmpeg4v3	--enable-decoder=hevc	--enable-encoder=libx265 \
--enable-encoder=h263   --enable-encoder=h263p	--enable-encoder=mpeg4 \
--enable-decoder=bmp	--enable-encoder=bmp	--enable-encoder=mpeg1video	--enable-encoder=mpeg2video \
--enable-decoder=tiff \
--enable-decoder=mp3  --enable-decoder=amrnb    \
--enable-encoder=aac  --enable-decoder=aac      \
--enable-swscale        --disable-yasm	 \
--enable-fft    --enable-rdft   --enable-mdct   --enable-neon \
--enable-network --enable-protocol=tcp --enable-demuxer=hls --enable-demuxer=rtsp --enable-demuxer=rtp --enable-demuxer=ac3 --enable-demuxer=dash \
--build-suffix=%{SUFFIX} \
%{?asan:--disable-inline-asm} \
"

%if 0%{?TIZEN_PRODUCT_TV}
export CONFIGURE_OPTIONS+="--enable-parser=vp8   --enable-decoder=vp8		--enable-decoder=vp9 "
%else
%endif

%ifarch %{arm} aarch64
export CONFIGURE_OPTIONS+="--disable-mmx "
%else
%endif

CFLAGS="%{optflags} -fPIC -d -DEXPORT_API=\"__attribute__((visibility(\\\"default\\\")))\" "; export CFLAGS

%ifarch %{arm}
export CONFIGURE_OPTIONS+="--extra-cflags=-mfpu=neon"
%endif

LDFLAGS="-Wl,-rpath,'\$\$\$\$ORIGIN'" ./configure \
    --prefix=%{_prefix} \
    --libdir=%_libdir \
    --shlibdir=%_libdir \
    $CONFIGURE_OPTIONS

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest packaging/ffmpeg.manifest
%defattr(-,root,root,-)
%{_bindir}/ff*
%{_datadir}/ffmpeg/*
%{_libdir}/libavcodec%{SUFFIX}.so.*
%{_libdir}/libavformat%{SUFFIX}.so.*
%{_libdir}/libavutil%{SUFFIX}.so.*
%{_libdir}/libavfilter%{SUFFIX}.so.*
%{_libdir}/libswscale%{SUFFIX}.so.*
%{_libdir}/libswresample%{SUFFIX}.so.*
%license COPYING.LGPLv2.1

%files devel
%defattr(-,root,root,-)
%_includedir/libavcodec/*
%_libdir/libavcodec%{SUFFIX}.so
%_libdir/pkgconfig/libavcodec%{SUFFIX}.pc
%_includedir/libavformat/*
%_libdir/libavformat%{SUFFIX}.so
%_libdir/pkgconfig/libavformat%{SUFFIX}.pc
%_includedir/libavutil/*
%_libdir/libavutil%{SUFFIX}.so
%_libdir/pkgconfig/libavutil%{SUFFIX}.pc
%_includedir/libavfilter/*
%_libdir/libavfilter%{SUFFIX}.so
%_libdir/pkgconfig/libavfilter%{SUFFIX}.pc
%_includedir/libswscale/*
%_libdir/libswscale%{SUFFIX}.so
%_libdir/pkgconfig/libswscale%{SUFFIX}.pc
%_includedir/libswresample/*
%_libdir/libswresample%{SUFFIX}.so
%_libdir/pkgconfig/libswresample%{SUFFIX}.pc
