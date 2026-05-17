graph TD
    %% Stil Tanımlamaları (GitHub Canlı Renkleri)
    classDef login fill:#4F46E5,stroke:#333,stroke-width:2px,color:#fff;
    classDef brain fill:#06B6D4,stroke:#333,stroke-width:2px,color:#fff;
    classDef core fill:#10B981,stroke:#333,stroke-width:2px,color:#fff;
    classDef detail fill:#F59E0B,stroke:#333,stroke-width:2px,color:#fff;
    classDef action fill:#EF4444,stroke:#333,stroke-width:2px,color:#fff;
    classDef admin fill:#EC4899,stroke:#333,stroke-width:2px,color:#fff;

    A[👋 1. Giriş Ekranı] -->|Rol Seçimi: Guest / User / Admin| B(🧠 2. Merkezi State / Hafıza)
    
    B --> C[🔍 3. Keşfet & Filtrele]
    C -->|Kategori / Arama / Sıralama| D[🗺️ 4. Destinasyon Detayı]
    
    D -->|Fallback Harita Sistemi| D1[🌐 WebEngine / Leaflet]
    D -->|İnternet/Kütüphane Yoksa| D2[🎨 QPainter 2D Çizim]
    
    D -->|💰 Akıllı Fiyat Hesaplama| E[🛒 5. Rezervasyon Yap]
    E -->|Kayıt Oluşturuldu| F[🧳 Rezervasyonlarım Sayfası]
    
    B -->|Sadece Yetkili Girişi| G[📊 6. Admin Yönetim Paneli]
    G -->|İstatistik & Destek| G1[🎫 Gelen Biletleri Yönet]

    %% Sınıf Atamaları
    class A login;
    class B brain;
    class C,F core;
    class D,D1,D2 detail;
    class E action;
    class G,G1 admin;
