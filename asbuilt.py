========================================================================
                      [ Cisco ThousandEyes Cloud ]
                      (Controladora SaaS / Portal)
========================================================================
           ^                        ^                        ^
           | TCP/443 (Outbound)     | TCP/443 (Outbound)     | TCP/443
           v                        v                        v
+--------------------+   +--------------------+   +--------------------+
| DATACENTER LOCAL   |   | NUVEM OCI (Oracle) |   | ESTAÇÕES / LAPTOPS |
| [ Enterprise Ag. ] |   | [ Enterprise Ag. ] |   | [ Endpoint Ags. ]  |
| IP: 10.1.0.25      |   | rhp-oci-te-lnx     |   | ~2.280 Usuários    |
+--------------------+   +--------------------+   +--------------------+
           |                        |                        |
           v                        v                        v
========================================================================
      ALVOS DE MONITORAMENTO (Targets) via ICMP, TCP, HTTP(S)
 [ Portais ] [ Applications Interno ] [ Cloud ] [ DNS Externo/Interno ]
========================================================================
    </pre>

    <p><strong>Código Estrutural (Mermaid) - Referência:</strong></p>
    <pre>
graph TD;
    TE[ThousandEyes SaaS Cloud] --> EA1[Enterprise Agent - On-Premises];
    TE --> EA2[Enterprise Agent - OCI];
    TE --> EPA[Endpoint Agents - 2.200+ Laptops];
    EA1 -->|Monitoramento| T1[SaaS Targets: M365, Salesforce];
    EA1 -->|Monitoramento| T2[Serviços Internos];
    EA2 -->|Monitoramento| T1;
    EA2 -->|Monitoramento| T2;
    EPA -->|AST / Wi-Fi| T1;
    </pre>