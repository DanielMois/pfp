// Configurações da aplicação PFP
const PFP_CONFIG = {
    // Opções de banco disponíveis
    BANCOS: [
        'Nubank',
        'Itaú'
    ],
    
    // Opções de categoria disponíveis
    CATEGORIAS: [
        'Alimentação',
        'Transporte Particular',
        'Transporte Público',
        'Dinheiro Emprestado',
        'Presente',
        'Moradia',
        'Saúde',
        'Educação',
        'Lazer',
        'Vestuário',
        'Tecnologia',
        'Serviços',
        'Bebida Alcoolica',
        'Futebol',
        'Outros'
    ],
    
    // Cores para gráficos - Famílias: Azul, Roxo, Cinza, Preto
    CORES_GRAFICO: [
        '#1E3A8A', // Azul escuro
        '#8B5CF6', // Roxo médio
        '#6B7280', // Cinza médio
        '#1F2937', // Cinza escuro
        '#3B82F6', // Azul médio
        '#A855F7', // Roxo claro
        '#9CA3AF', // Cinza claro
        '#111827', // Preto suave
        '#1D4ED8', // Azul profundo
        '#9333EA', // Roxo profundo
        '#4B5563', // Cinza neutro
        '#000000', // Preto puro
        '#60A5FA', // Azul claro
        '#C084FC', // Roxo muito claro
        '#D1D5DB'  // Cinza muito claro
    ],
    
    // Cores para gráfico de bancos
    CORES_BANCOS: [
        '#8A2BE2', // Nubank - Roxo característico
        '#FF8C00'  // Itaú - Laranja característico
    ],
    
    // Configurações para modo escuro
    MODO_ESCURO: {
        // Cores de fundo para gráficos no modo escuro
        CORES_FUNDO: [
            '#2D2D2D', // Fundo escuro
            '#1A1A1A', // Fundo mais escuro
            '#404040', // Fundo médio escuro
            '#333333'  // Fundo neutro escuro
        ],
        
        // Cores de texto para gráficos no modo escuro
        CORES_TEXTO: [
            '#FFFFFF', // Texto branco
            '#E0E0E0', // Texto cinza claro
            '#B0B0B0', // Texto cinza médio
            '#CCCCCC'  // Texto cinza suave
        ]
    }
};

// Função para preencher select com opções
function preencherSelect(selectElement, options, placeholder = 'Selecione...') {
    selectElement.innerHTML = `<option value="">${placeholder}</option>`;
    options.forEach(option => {
        selectElement.innerHTML += `<option value="${option}">${option}</option>`;
    });
}

// Função para obter cor baseada no índice
function obterCor(indice, arrayCores = PFP_CONFIG.CORES_GRAFICO) {
    return arrayCores[indice % arrayCores.length];
}

// Função para obter cor de uma categoria específica
function obterCorCategoria(categoria) {
    const indice = PFP_CONFIG.CATEGORIAS.indexOf(categoria);
    if (indice === -1) return '#6B7280'; // Cinza padrão se não encontrar
    return PFP_CONFIG.CORES_GRAFICO[indice];
}

// Função para obter cor de um banco específico
function obterCorBanco(banco) {
    const indice = PFP_CONFIG.BANCOS.indexOf(banco);
    if (indice === -1) return '#6B7280'; // Cinza padrão se não encontrar
    return PFP_CONFIG.CORES_BANCOS[indice];
}

// Função para verificar se está no modo escuro
function isModoEscuro() {
    return document.documentElement.getAttribute('data-theme') === 'dark';
}

// Função para obter configurações de tema para gráficos
function obterConfiguracaoTema() {
    const modoEscuro = isModoEscuro();
    
    if (modoEscuro) {
        return {
            backgroundColor: PFP_CONFIG.MODO_ESCURO.CORES_FUNDO[0],
            borderColor: PFP_CONFIG.MODO_ESCURO.CORES_FUNDO[1],
            color: PFP_CONFIG.MODO_ESCURO.CORES_TEXTO[0],
            grid: {
                color: PFP_CONFIG.MODO_ESCURO.CORES_TEXTO[2]
            }
        };
    } else {
        return {
            backgroundColor: '#ffffff',
            borderColor: '#e9ecef',
            color: '#212529',
            grid: {
                color: '#dee2e6'
            }
        };
    }
} 