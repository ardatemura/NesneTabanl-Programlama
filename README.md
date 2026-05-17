graph LR
    %% Renk Renklendirmeleri
    classDef gate fill:#2e3440,stroke:#81a1c1,stroke-width:2px,color:#d8dee9;
    classDef core fill:#3b4252,stroke:#88c0d0,stroke-width:2px,color:#e5e9f0;
    classDef map fill:#434c5e,stroke:#a3be8c,stroke-width:2px,color:#e5e9f0;
    classDef calc fill:#4c566a,stroke:#ebcb8b,stroke-width:2px,color:#e5e9f0;

    A[🔑 Giriş Paneli] -->|Rol Dağıtımı| B(🧠 Merkezi State);
    
    B --> C[🏠 Keşif Ekranı];
    C -->|Filtreleme / Sıralama| D[📄 Destinasyon Detay];
    
    D --> E{🌐 Harita Motoru};
    E -->|WebEngine Aktif| F[🗺️ Canlı Leaflet Harita];
    E -->|WebEngine Eksik| G[🎨 2D Fallback Çizim];
    
    D --> H[💰 Dinamik Fiyat Hesaplama];
    H -->|Rezervasyon Onay| I[🗃️ Rezervasyonlarım];

    class A,B gate;
    class C,D,I core;
    class E,F,G map;
    class H calc;
