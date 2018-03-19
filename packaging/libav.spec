Name:       libav
Summary:    AV codec lib
Version:    11.4
Release:    0
Group:      Multimedia/Libraries
URL:        http://libav.org
License:    LGPL-2.1+
Source0:    %{name}-%{version}.tar.gz

%description
AV codec library

%package -n libavtools
Summary:    AV tools
Group:      Multimedia/Libraries

%description -n libavtools
AV tools binary

%package -n libavcodec
Summary:    AV codec lib
Group:      Multimedia/Libraries

%description -n libavcodec
AV codec library

%package -n libavcodec-devel
Summary:    AV codec lib (devel)
Group:      Multimedia/Libraries
Requires:   libavcodec = %{version}-%{release}

%description -n libavcodec-devel
AV codec library (devel)

%package -n libavformat
Summary:    AV format lib
Group:      Multimedia/Libraries

%description -n libavformat
AV format library

%package -n libavformat-devel
Summary:    AV format lib (devel)
Group:      Multimedia/Libraries
Requires:   libavformat = %{version}-%{release}

%description -n libavformat-devel
AV format library (devel)

%package -n libavutil
Summary:    AV util lib
Group:      Multimedia/Libraries

%description -n libavutil
AV util library

%package -n libavutil-devel
Summary:    AV util lib (devel)
Group:      Multimedia/Libraries
Requires:   libavutil = %{version}-%{release}

%description -n libavutil-devel
AV util library (devel)

%package -n libavfilter
Summary:    AV util lib
Group:      Multimedia/Libraries

%description -n libavfilter
AV filter library

%package -n libavfilter-devel
Summary:    AV util lib (devel)
Group:      Multimedia/Libraries
Requires:   libavfilter = %{version}-%{release}

%description -n libavfilter-devel
AV filter library (devel)

%package -n libswscale
Summary:    SW scale lib
Group:      Multimedia/Libraries

%description -n libswscale
development files for libswsacle

%package -n libswscale-devel
Summary:    SW scale lib (devel)
Group:      Multimedia/Libraries
Requires:   libswscale = %{version}-%{release}

%description -n libswscale-devel
development files for libswsacle

%package -n libswresample
Summary:    SW resample lib
Group:      Multimedia/Libraries

%description -n libswresample
development files for libswresample

%package -n libswresample-devel
Summary:    SW resample lib (devel)
Group:      Multimedia/Libraries
Requires:   libswresample = %{version}-%{release}

%description -n libswresample-devel
development files for libswresample

%define SUFFIX -juvo

%prep
%setup -q

export CONFIGURE_OPTIONS="--enable-shared    --disable-static   \
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

./configure \
    --prefix=%{_prefix} \
    --libdir=%_libdir \
    --shlibdir=%_libdir \
    $CONFIGURE_OPTIONS

%build


%__make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -n libavtools
%manifest packaging/libavtools.manifest
%defattr(-,root,root,-)
%{_bindir}/ff*
%{_datadir}/ffmpeg/*

%files -n libavcodec
%manifest packaging/libavcodec.manifest
%defattr(-,root,root,-)
%{_libdir}/libavcodec%{SUFFIX}.so.*
%license COPYING.LGPLv2.1
%post -n libavcodec -p /sbin/ldconfig
%postun -n libavcodec -p /sbin/ldconfig

%files -n libavformat
%manifest packaging/libavformat.manifest
%defattr(-,root,root,-)
%{_libdir}/libavformat%{SUFFIX}.so.*
%license COPYING.LGPLv2.1
%post -n libavformat -p /sbin/ldconfig
%postun -n libavformat -p /sbin/ldconfig

%files -n libavutil
%manifest packaging/libavutil.manifest
%defattr(-,root,root,-)
%{_libdir}/libavutil%{SUFFIX}.so.*
%license COPYING.LGPLv2.1
%post -n libavutil -p /sbin/ldconfig
%postun -n libavutil -p /sbin/ldconfig

%files -n libavfilter
%manifest packaging/libavfilter.manifest
%defattr(-,root,root,-)
%{_libdir}/libavfilter%{SUFFIX}.so.*
%license COPYING.LGPLv2.1
%post -n libavfilter -p /sbin/ldconfig
%postun -n libavfilter -p /sbin/ldconfig

%files -n libswscale
%manifest packaging/libswscale.manifest
%defattr(-,root,root,-)
%{_libdir}/libswscale%{SUFFIX}.so.*
%license COPYING.LGPLv2.1
%post -n libswscale -p /sbin/ldconfig
%postun -n libswscale -p /sbin/ldconfig

%files -n libswresample
%manifest packaging/libswresample.manifest
%defattr(-,root,root,-)
%{_libdir}/libswresample%{SUFFIX}.so.*
%license COPYING.LGPLv2.1
%post -n libswresample -p /sbin/ldconfig
%postun -n libswresample -p /sbin/ldconfig

%files -n libavcodec-devel
%defattr(-,root,root,-)
%_includedir/libavcodec/*
%_libdir/libavcodec%{SUFFIX}.so
%_libdir/pkgconfig/libavcodec%{SUFFIX}.pc

%files -n libavformat-devel
%defattr(-,root,root,-)
%_includedir/libavformat/*
%_libdir/libavformat%{SUFFIX}.so
%_libdir/pkgconfig/libavformat%{SUFFIX}.pc

%files -n libavutil-devel
%defattr(-,root,root,-)
%_includedir/libavutil/*
%_libdir/libavutil%{SUFFIX}.so
%_libdir/pkgconfig/libavutil%{SUFFIX}.pc

%files -n libavfilter-devel
%defattr(-,root,root,-)
%_includedir/libavfilter/*
%_libdir/libavfilter%{SUFFIX}.so
%_libdir/pkgconfig/libavfilter%{SUFFIX}.pc

%files -n libswscale-devel
%defattr(-,root,root,-)
%_includedir/libswscale/*
%_libdir/libswscale%{SUFFIX}.so
%_libdir/pkgconfig/libswscale%{SUFFIX}.pc

%files -n libswresample-devel
%defattr(-,root,root,-)
%_includedir/libswresample/*
%_libdir/libswresample%{SUFFIX}.so
%_libdir/pkgconfig/libswresample%{SUFFIX}.pc

